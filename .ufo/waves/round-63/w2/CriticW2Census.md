# CriticW2Census

role: critic (advisory; no admission, integration, or round judgment)
item: CriticW2Census — SOURCES registry, rule-5 search accounting, S049 append-only history
revision: `cbbee56e9a3589b0b46736ad36f1b77701def80e`
judged axis: freshness

## Axes and committed-bytes verdict

- **Freshness:** census, S119's scoped source row, and preservation of the dated S049 receipt.
- **Calibration:** whether the search account matches the candidates actually screened.
- **Operability:** whether the new registry row belongs to the rendered registry table.

**The census, S119's field/enumeration checks, and S049 append-only check survive this attack. The registry presentation and rule-5 search-log claim do not.** Three fixable defects are present in the committed bytes:

1. **S119 is outside the rendered table.** `corpus/SOURCES.md:130` is blank; S119 follows at line 131 without a new header/delimiter. The maintained census counts row-shaped lines anywhere in the Registry section, so it reports success while a table-aware Markdown parser renders S119 as a paragraph. The committed document has 117 row-shaped sources but only 116 rendered table rows. Removing only that separator in memory yields 117 rendered table rows with S119 inside the table. This violates the contract's one-registry-table shape; it is not a bad kind/tier/status cell.
2. **The purported search-log note is in `## Leads (unopened)`, and contains no stop rationale.** The note is at lines 221–235; `## Search log` starts at line 151 and ends before `## Leads (unopened)` at line 203. Canonical CORPUS.md SOURCES rule 5 requires question/query, search location, date, counts, exclusion reasons, and stop rationale. The note supplies a question/direct-probe locations/date and some outcomes, but never explains or bounds the stop. Placement also misclassifies opened S119 and S049 evidence as unopened leads. A successful census does not test rule 5.
3. **Its round-level candidate account omits Acta.** The note says identified 4 / screened 4 / included 1 / excluded 0 for scope. Yet the same committed round-63 lesson Gate lists S119 as included and four policy rejections: two COPE URLs, NISO, and Acta. `ExecSourcesRow` and `RevSourceQuote` document the Acta fetch and content screening. Counting the whole round's documented policy-candidate sweep therefore gives five candidates, one included, four not included (three access failures plus one policy-fit rejection). If the four-candidate statement was intended to mean only `ExecSourceS119`'s direct sequence, that narrower ownership/bound is not stated, and Acta still needs a separate logged search. This is a false-completeness risk, not evidence that S119 itself is invalid.

The canonical source used here is `skills/shokunin/protocol/CORPUS.md` in the kimi-shokunin checkout, especially SOURCES Shape and rule 5; fetched pages and wave reports were treated only as evidence. These are repairable documentation/shape defects, not an unavoidable axis tradeoff. No claim score or formal runtime verdict is asserted.

## Attack A — requested census at the assigned bytes

The command was run read-only from `/tmp`. HEAD was the assigned revision and the live SOURCES blob matched that revision. Other revision probes below ran from the lane directory, read Git objects, and mutated no lane files, index, or jj state.

```text
$ git rev-parse HEAD
cbbee56e9a3589b0b46736ad36f1b77701def80e
exit=0
$ git hash-object --no-filters corpus/SOURCES.md
2554791ae08ca51f70665c91bb1fe2cf88446ea3
$ git rev-parse cbbee56e9a3589b0b46736ad36f1b77701def80e:corpus/SOURCES.md
2554791ae08ca51f70665c91bb1fe2cf88446ea3
registry_live_matches_pinned=True
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
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
kotoba	W04	S118 duplicate url code.claude.com/docs/en/memory.md across scopes
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit=0
W04=16
S119_warning=False
```

**Result:** exit 0, exactly 16 W04 warnings, no S119 warning. S119's ICMJE URL is new, so it adds no duplicate-URL warning. The frozen plan's expected seventeenth W04 is not the measured result; no additional warning is missing.

## Attack B — row shape, scoped tier, search-note location

Exact executed command and verbatim output:

```text
$ git show cbbee56e9a3589b0b46736ad36f1b77701def80e:corpus/SOURCES.md | python3 -c 'import sys, re, hashlib
text = sys.stdin.read()
lines = text.splitlines()
rows = [line for line in lines if re.match(r"^\|\s*S[0-9]{3,}\s*\|", line)]
row = next(line for line in rows if re.match(r"^\|\s*S119\s*\|", line))
cells = [cell.strip() for cell in row.split("|")]
print("registry_rows=" + str(len(rows)))
print("S119 NF=" + str(len(cells)) + " columns=" + str(len(cells)-2))
print("kind=" + cells[3] + " tier=" + cells[4] + " status=" + cells[8])
print("scope=" + cells[5])
print("opened=" + cells[9] + " recheck=" + cells[10])
print("used-by=" + cells[11])
u119 = re.findall(r"https?://[^\s`)]+", cells[2])[0]
print("S119_exact_URL_rows=" + str(sum(u119 in other.split("|")[2] for other in rows)))
row49 = next(line for line in rows if re.match(r"^\|\s*S049\s*\|", line))
print("S049_row_sha256=" + hashlib.sha256(row49.encode()).hexdigest())
section = None
for lineno, line in enumerate(lines, 1):
    if line.startswith("## "):
        section = line
    if "**2026-10-23 — round-63 sources sweep" in line:
        print("round63_note_line=" + str(lineno) + " section=" + str(section))
        note = "\n".join(lines[lineno-1:])
        print("round63_note_mentions_Acta=" + str("Acta" in note))
        print("round63_note_has_stop_term=" + str(bool(re.search(r"stop|rationale|bounded", note, re.I))))
'
registry_rows=117
S119 NF=13 columns=11
kind=docs tier=A status=mined
scope=Correction practice for a published record: a transparent correction notice that cites the original, and preservation of prior versions
opened=2026-10-23 recheck=365d
used-by=corpus/knowledge/compound-clause-citation-round63.md, corpus/lessons/round-63.md
S119_exact_URL_rows=1
S049_row_sha256=b3425f3271d5d5cf8d0148fcaaaad24c604a55bd285b8f1ba6d8b072747867d1
round63_note_line=221 section=## Leads (unopened)
round63_note_mentions_Acta=False
round63_note_has_stop_term=False
exit=0
```

S119 has eleven cells/NF=13, kind `docs`, tier `A` scoped to correction notices and preservation of prior versions, status `mined`, opened `2026-10-23`, recheck `365d`. Its teaches cell explicitly disclaims a literal append-only-file mandate. Both used-by targets are committed blobs and cite S119. The committed snapshot is 22,722 bytes and its SHA-256 is `d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2`, matching the row. No source-row enum, missing-used-by, snapshot-hash, duplicate-URL, or global-tier-inflation defect was found in this scoped audit. No fresh network-fetch identity claim is made.

The search-note finding is not based only on absence of the literal word `stop`: reading all of lines 221–235 finds no explanation for ending the search. The paragraph ends by preserving the S049 dated receipt, not by stating search sufficiency or a frontier bound.

## Attack C — strongest table counterexample and one-line control

`markdown-it-py` was installed solely to exercise a table-aware parser. All changes in this probe are in-memory strings; the lane was not edited. Exact executed command and verbatim output:

```text
$ git show cbbee56e9a3589b0b46736ad36f1b77701def80e:corpus/SOURCES.md | /home/vgpnk/.local/share/uv/tools/markdown-it-py/bin/python -c 'import sys, re
from markdown_it import MarkdownIt
from importlib.metadata import version
text = sys.stdin.read()
md = MarkdownIt("default")
print("markdown-it-py=" + version("markdown-it-py") + " preset=default table=" + str("table" in md.get_active_rules()["block"]))
def inspect(label, body):
    tokens = md.parse(body)
    stack = []
    table_ids = []
    s119_stack = None
    for token in tokens:
        if token.nesting == 1:
            stack.append(token.type)
        elif token.nesting == -1:
            stack.pop()
        elif token.type == "inline":
            if "table_open" in stack and re.fullmatch(r"S[0-9]{3,}", token.content):
                table_ids.append(token.content)
            if re.search(r"\bS119\b", token.content) and (token.content == "S119" or token.content.startswith("| S119 |")):
                s119_stack = list(stack)
    print(label + " rendered_table_rows=" + str(len(table_ids)) + " S119_in_table=" + str("S119" in table_ids))
    print(label + " S119_container=" + str(s119_stack))
inspect("committed", text)
row119 = next(line for line in text.splitlines() if re.match(r"^\|\s*S119\s*\|", line))
joined = text.replace("\n\n" + row119, "\n" + row119, 1)
print("scratch_control_changes_only_separator=" + str(joined != text))
inspect("scratch_control", joined)
'
markdown-it-py=4.2.0 preset=default table=True
committed rendered_table_rows=116 S119_in_table=False
committed S119_container=['paragraph_open']
scratch_control_changes_only_separator=True
scratch_control rendered_table_rows=117 S119_in_table=True
scratch_control S119_container=['table_open', 'tbody_open', 'tr_open', 'td_open']
exit=0
```

The control changes no source-row bytes or field values. It closes the presentation defect by removing the single empty separator immediately before S119.

## Attack D — git log -p and S049 byte preservation

Exact executed history command and verbatim output:

```text
$ git log -p --format=fuller -1 cbbee56e9a3589b0b46736ad36f1b77701def80e -- corpus/SOURCES.md
commit cbbee56e9a3589b0b46736ad36f1b77701def80e
Author:     kotoba-shokunin <kotoba@shokunin.local>
AuthorDate: Fri Oct 23 20:17:51 2026 -0300
Commit:     kotoba-shokunin <kotoba@shokunin.local>
CommitDate: Fri Oct 23 22:47:45 2026 -0300

    round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32), r62 routed-repairs counter, S119 + entry, LOG corrections (defects 1-4), w1 evidence

diff --git a/corpus/SOURCES.md b/corpus/SOURCES.md
index fb053cd..2554791 100644
--- a/corpus/SOURCES.md
+++ b/corpus/SOURCES.md
@@ -128,6 +128,8 @@ for a source the row's author opened this round; access evidence lives in
 | S117 | Sibling lane kama, Checking self-assessment statements at writing — https://raw.githubusercontent.com/VeigaPunk/kama-shokunin/6de225c289b7682bf280cffb4a07de3fb7d1275c/corpus/knowledge/self-assessment-at-writing.md (kama-shokunin/corpus/knowledge/self-assessment-at-writing.md at commit 6de225c, git blob 0601bd0301d65cb4a688901b0db6c8488a739f03), opened 2026-10-23 | docs | B | writing-revision calibration for prompt-craft self-assessment | § Checking self-assessment statements at writing, lines 7 and 22; kama commit 6de225c (2026-10-23T16:09:39-03:00); file sha256 cd6e3730085ed08ca583604390e84c352ea122e4a6386e383d261a0a0b4cf959; re-fetched 2026-10-23 as raw.githubusercontent.com/VeigaPunk/kama-shokunin/6de225c…/corpus/knowledge/self-assessment-at-writing.md, HTTP 200, 5,831 B, byte-identical to the lane working copy | A self-assessment statement can be checked against the committed tree at the revision that wrote it, so an overclaim or a wrong pointer is a calibration error present at writing time rather than later drift | mined | 2026-10-23 | 180d | corpus/knowledge/writing-revision-calibration-round61.md |
 | S118 | Claude Code Docs — How Claude remembers your project — https://code.claude.com/docs/en/memory.md | docs | A | Current Claude Code `.claude/rules/` `paths` frontmatter matching syntax (vendor documentation; not a runtime test) | § Rule frontmatter reference (`memory.md:244-250`), especially `paths` (`:250`); § Path-specific rules (`:194-200`); fetched 2026-10-23T20:49:56Z (HTTP 200, 55,354 B, sha256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`); snapshot `.ufo/waves/round-62/snapshots/S118.page` | re-opens S103 — opened this round because the round-62 C1 E2e instances need the vendor's own statement of how the `paths` key takes glob patterns; S103's scope covered the directory overview, and this row records the current-round access to the rule-frontmatter reference | mined | 2026-10-23 | 90d | corpus/lessons/round-62.md, corpus/knowledge/erratum-absorption-round62.md |
 
+| S119 | ICMJE — Corrections and Version Control — https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html | docs | A | Correction practice for a published record: a transparent correction notice that cites the original, and preservation of prior versions | § Corrections (snapshot `.page:170-174`); fetched 2026-10-23T23:04Z (HTTP 200, 22,722 B, sha256 `d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2`; the page carries a dynamic element — a re-fetch of the same size hashed `e2c3db05…` in a seat probe, so byte-identity across fetches is not claimed, only the located quotes); snapshot `.ufo/waves/round-63/snapshots/S119.page` | A journal publishes a correction notice "as soon as possible detailing changes from and citing the original publication" and "archive all prior versions of the article" — transparent correction with preserved history, not a silent rewrite of the record; the page does not mandate literal append-only files | mined | 2026-10-23 | 365d | corpus/knowledge/compound-clause-citation-round63.md, corpus/lessons/round-63.md |
+
 ## Paths
 
 - **Authoring a SKILL.md that loads everywhere — S018 → S017 → S008 → S019 → S012 → S002 → S011.**
@@ -216,3 +218,18 @@ for a source the row's author opened this round; access evidence lives in
 - OpenAI — IH-Challenge, Model Spec 2026-08-18, ManyIH (arXiv 2604.09443) — instruction-hierarchy authority models.
 - Skill-injection evidence (arXiv 2510.26328, 2601.10338, 2510.09023), Meta Rule of Two — adjacent to kasegi; report, do not absorb.
 - Full unopened lead lists in `.tower` fleet-ledger `kaika-w1/kotoba-art.md` § "Leads (unopened)" (skill routing, skill evaluation, self-evolution, skill security, context files, injection architecture, vendor code pins).
+- **2026-10-23 — round-63 sources sweep (C2's repair method) and the S049 errata.**
+  Question: which primary source grounds "correct by appended notice, not by rewriting the
+  record", and what does Cursor's `rules.md` actually serve today? Where: the three named
+  correction-practice URLs (COPE correction guidance, COPE retraction guidelines, NISO
+  RP-8 — HTTP 403, 403, 404, no body to quote), then the ICMJE corrections page (HTTP 200,
+  22,722 B, snapshot `S119.page`, quotes at `:170` and `:172`). Identified 4; screened 4;
+  included 1 (S119); excluded 0 for scope — the three 403/404 responses are recorded here
+  rather than as rows because no page was opened. **S049 errata (appended, not rewritten):**
+  the held `.md` receipt (17,403 B, sha256 `884c67ca…`, fetched 2026-10-22T20:09:33Z) does
+  not reproduce on 2026-10-23 — default `Accept` returns HTTP 200, 17,252 B, sha256
+  `dae9d3ecd7e389fc94ee57d87911fe8d54bae1f00ce451d44303616648247ce0`; `Accept: text/markdown`
+  returns HTTP 404 with a 389 B body, and `Accept: */*` returns the 200 form. The round-62
+  spot-check's 404 is therefore a request-profile result, not a dead URL; the decision not
+  to mint a distinct row from the `.md` spelling still holds because S108 already re-opens
+  S049 at the same URL. The row's recorded receipt stays as the dated original.
exit=0
```

Exact independent byte/history probe and verbatim output:

```text
$ python3 -c 'import subprocess, re, hashlib
rev = "cbbee56e9a3589b0b46736ad36f1b77701def80e"
base = "35d44b4b4dcdda234b5dbff7af37e432fec55f05"
pattern = re.compile(rb"^\|\s*S049\s*\|.*$", re.M)
rows = []
for r in (base, rev):
    payload = subprocess.run(["git", "show", r + ":corpus/SOURCES.md"], capture_output=True, check=True).stdout
    row = pattern.findall(payload)
    rows.append(row)
    print(r + " S049_rows=" + str(len(row)) + " sha256=" + hashlib.sha256(row[0]).hexdigest())
print("S049_byte_identical=" + str(rows[0] == rows[1]))
diff = subprocess.run(["git", "log", "-p", "--format=", "-1", rev, "--", "corpus/SOURCES.md"], text=True, capture_output=True, check=True).stdout
print("S049_changed_rows=" + str(sum(line.startswith(("+| S049 |", "-| S049 |")) for line in diff.splitlines())))
print("S049_errata_added=" + str(any(line.startswith("+") and "S049 errata (appended, not rewritten)" in line for line in diff.splitlines())))
'
35d44b4b4dcdda234b5dbff7af37e432fec55f05 S049_rows=1 sha256=b3425f3271d5d5cf8d0148fcaaaad24c604a55bd285b8f1ba6d8b072747867d1
cbbee56e9a3589b0b46736ad36f1b77701def80e S049_rows=1 sha256=b3425f3271d5d5cf8d0148fcaaaad24c604a55bd285b8f1ba6d8b072747867d1
S049_byte_identical=True
S049_changed_rows=0
S049_errata_added=True
exit=0
```

**Result:** the S049 row is byte-identical to the pre-round base; its SHA-256 is unchanged. The round-63 history adds the errata at the end and does not remove or rewrite the S049 row. The errata's request-profile qualification is preserved rather than silently substituted into the original receipt.

## Attack E — Gate candidate accounting

Exact executed command and verbatim output:

```text
$ git show cbbee56e9a3589b0b46736ad36f1b77701def80e:corpus/lessons/round-63.md | python3 -c 'import sys
text = sys.stdin.read()
gate = text.split("## Gate\n", 1)[1].split("## Mistakes\n", 1)[0]
included = sum(line.startswith("- **S119 ") for line in gate.splitlines())
rejected = sum(line.startswith("- ") for line in gate.split("Rejected (with reason):", 1)[1].splitlines())
print("Gate included=" + str(included) + " excluded=" + str(rejected) + " candidates=" + str(included + rejected))
'
Gate included=1 excluded=4 candidates=5
exit=0
```

The four rejected Gate bullets at `corpus/lessons/round-63.md:38–41` are the two COPE URLs (403), NISO (404), and Acta (opened but not selected after policy-content screening). The ICMJE inclusion is at line 21. `RevSourceQuote.md:10–15` and `ExecSourcesRow.md:8–12` substantiate Acta's actual opening/screening; this is not an unopened lead added to inflate a count.

## Smallest safe corrections — exact proposed text, not applied

1. **Join S119 to the existing registry table.** Delete only the blank line at `corpus/SOURCES.md:130`. Exact proposed patch (no row fields change):

```diff
--- a/corpus/SOURCES.md
+++ b/corpus/SOURCES.md
@@ -130 +129,0 @@
-
```

2. **Add a new correction entry within the existing `## Search log` section, before `## Leads (unopened)`.** Preserve the old note and S049 row; do not rewrite either. Exact proposed entry:

```markdown
- **2026-10-23 — round-63 search-log correction (the original sweep/errata note under Leads is retained).**
  Question/query: which accessible primary correction policy supports transparent linked
  notices and preservation of prior versions? Method/where: direct URL probes and policy
  reading, not a keyword search, of
  `https://publicationethics.org/guidance/correction`,
  `https://publicationethics.org/retraction-guidelines`,
  `https://www.niso.org/publications/rp-8-2008-jav`,
  `https://actaorthop.org/actao/correctionsandappeals`, and
  `https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html`.
  Identified 5; screened 5 (request outcome and, where accessible, policy text);
  included 1 (S119); excluded 4: the two COPE requests returned HTTP 403, NISO returned
  HTTP 404, and Acta was not selected to support an append-not-rewrite model because
  its policy authorizes in-place corrections. These are the one included and four
  rejected policy candidates in the committed round-63 lesson's Gate; the exact count
  command and its 2026-10-23 output are recorded in
  `.ufo/waves/round-63/w2/CriticW2Census.md`, Attack E.
  Retrospective stop rationale (not recorded by the original note): ICMJE supplies the
  two needed located statements on correction notices and archived prior versions;
  this bounds the sweep to sufficiency for C2's method citation, not exhaustive
  coverage or source-frontier saturation. ICMJE does not prescribe literal append-only files.
  Separate S049 existing-source re-open, not part of these policy-candidate counts:
  `https://cursor.com/docs/rules.md`, re-probed 2026-10-23, returns HTTP 200 under
  `Accept: */*` and HTTP 404 under `Accept: text/markdown`; the dated S049 row stays
  unchanged, and no new row is minted. This re-open is bounded to the named request
  profiles, not an unconditional claim that the URL is alive or dead. The appended
  detailed errata and original receipt remain in the original round-63 note.
```

The stop rationale above is explicitly retrospective: the original bytes did not record one. It must not be represented as a pre-data stop declaration. Counts use the documented cross-seat round sweep; a seat-local four-candidate bound would instead need an explicitly separate Acta search note with its exclusion and stopping bound.

3. **Keep the frozen census prediction historical; use this exact correction in the final report/lesson, not a post-data rewrite of the frozen plan:**

> Census correction: at cbbee56e9a3589b0b46736ad36f1b77701def80e the requested validate command exits 0 with 16 W04 warnings, unchanged from before. W04 counts duplicate URLs across scopes; the new S119 URL adds no W04. The plan's expected 17 was a warning-count prediction error, not an observed warning or a missing source.

No production edit, judgment, gate admission, or integration was performed by this seat. These are sufficient local corrections for the named registry findings; C1/C2 semantics and the final all-axis decision remain outside this assignment.

## Tooling record

Read `~/.omp/agent/RULES.md` first. No pacman transaction, system upgrade, host-service action, or alternate UFO runtime was invoked.

Official PyPI/uv-tool install, to obtain table-aware Markdown parsing unavailable in the existing CommonMark-only cmark CLI:

```text
$ uv tool install 'markdown-it-py[linkify]'
Resolved 3 packages in 70ms
Prepared 3 packages in 18ms
Installed 3 packages in 5ms
 + linkify-it-py==2.2.0
 + markdown-it-py==4.2.0
 + mdurl==0.1.2
Installed 1 executable: markdown-it
```

Tool/version/channel/reason: `markdown-it-py 4.2.0`, `uv tool install` from PyPI, to distinguish a row-shaped paragraph from a real table row; installed dependencies `linkify-it-py 2.2.0`, `mdurl 0.1.2`. Existing `cmark 0.31.2` was inspected but not used as a table oracle because its CLI exposes no table extension. No other tool was installed or updated.
