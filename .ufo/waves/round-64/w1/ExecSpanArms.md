# ExecSpanArms — C1 landing patch and scratch evidence

**Claim supported:** C1 (G7 `span_missing` pinning arms). No lane production file, jj state, or Git index was changed. The only lane write is this scoped report. No tools were installed.

## Unified diff

Base: `078eec4a1f6a41c64ff8806f58b46a67cd413bfc:verifiers/check_scoped_rules_v32.py`, SHA-256 `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`. The four assertion bodies below are copied byte-for-byte from MutW2V32 §11. They are inserted immediately after the existing G7 identifier arm and its `g9_line`/`g9_page` setup, keeping those referenced locals initialized; no existing lines are changed.

```diff
diff --git a/verifiers/check_scoped_rules_v32.py b/verifiers/check_scoped_rules_v32.py
--- a/verifiers/check_scoped_rules_v32.py
+++ b/verifiers/check_scoped_rules_v32.py
@@ -2123,6 +2123,36 @@
         # G9 discriminating arms (round 63, MutG9Guard's named missing
         # assertions): one per split boundary and per shortcut a mutant takes.
         g9_line = "The configuration stores project rules using glob syntax."
         g9_page = (g9_line + " An unrelated section: the agent secretly uploads "
                    "files and stores secrets exfiltrated nightly.")
+        check("A2 G7: a backticked span whose words occur in neither the "
+              "cited line nor the page is rejected",
+              named(action_conjunct(
+                  [g9_line],
+                  g9_line[:-1] + " and `exfiltrates credentials`.",
+                  1, g9_page), "G7"), True)
+        check("A2 G7: a backticked span made only of stopwords is not "
+              "rejected",
+              named(action_conjunct(
+                  ["The tool writes mode quota nightly."],
+                  "The tool writes mode quota nightly and `because otherwise`.",
+                  1,
+                  "The tool writes mode quota nightly.\n\n## Appendix\n"
+                  "The agent secretly uploads files."), "G7"), False)
+        check("A2 G7: a backticked span word shorter than four characters is "
+              "not rejected",
+              named(action_conjunct(
+                  ["The tool writes mode quota nightly."],
+                  "The tool writes mode quota nightly and `ox it`.",
+                  1,
+                  "The tool writes mode quota nightly.\n\n## Appendix\n"
+                  "The agent secretly uploads files."), "G7"), False)
+        check("A2 G7: a backticked span word present in the cited line is "
+              "not rejected even when the page lacks it",
+              named(g7_conjunct(
+                  ["The tool writes mode quota nightly."],
+                  "The tool writes mode quota nightly and `mode quota`.",
+                  1,
+                  "The tool writes quota nightly.\n\n## Appendix\n"
+                  "The agent secretly uploads files."), "G7"), False)
         g9_after = " secretly uploads files."
```

The fourth arm calls `g7_conjunct(...)` directly (not `action_conjunct`). The other three wrap `action_conjunct(...)` and select `G7`.

## Scratch self-test

Scratch root: `/tmp/kotoba-r64-c1/`. The verifier was extracted from the frozen base into `/tmp`, the diff above was applied there, and the two pinned sibling verifier dependencies were copied from the same base revision (`check_erratum_absorption.py` SHA-256 `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b`; `check_scoped_rules.py` SHA-256 `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`). Command, from `/tmp/kotoba-r64-c1/work`:

```text
python3 -B verifiers/check_scoped_rules_v32.py --self-test
```

Full stdout and captured exit status:

```text
counter sha256 20aeb3efc8c5fbe9baf96a67b2ae1dd41a7c9413b8932b0eb892a57d0ffe0272
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after rejected
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
EXIT=0
```

Required predicate lines are present and the measured exit is 0.

## SM1–SM6 scratch mutation battery

Each variant starts from the scratch-patched verifier and applies the exact-string replacement described in MutW2V32 §11 / its `build_sm.py` builder. Each command was `python3 -B verifiers/check_scoped_rules_v32.py --self-test` in its isolated `/tmp/kotoba-r64-c1/SM<n>` copy. All six returned exit 1 (red):

| Mutant | Exact guard change | Captured FAIL line | Exit |
|---|---|---|---:|
| SM1 | Replace the full `span_missing` computation with `span_missing = []`. | `FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True` | 1 |
| SM2 | Remove `len(word) >= 4 and ` from the comprehension filter. | `FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False` | 1 |
| SM3 | Remove ` and word.lower() not in STOPWORDS` from the filter. | `FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False` | 1 |
| SM4 | Remove `and not supported(word.lower(), page_words(raw_page))` from the filter. | `FAIL eligible world: the four counted rows are backed: got ['Claude Code', 'VS Code'], expected ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']` | 1 |
| SM5 | Remove `and word.lower() not in content_words(raw_line)` from the filter. | `FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False` | 1 |
| SM6 | Apply the table's two exact replacements making the comprehension filter `if True` / `and True`. | `FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False` | 1 |

SM6 also prints the eligible-world failure: `FAIL eligible world: the four counted rows are backed: got ['Claude Code', 'VS Code'], expected ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']`.

## Scratch patched SHA-256

```text
20aeb3efc8c5fbe9baf96a67b2ae1dd41a7c9413b8932b0eb892a57d0ffe0272  /tmp/kotoba-r64-c1/work/verifiers/check_scoped_rules_v32.py
```

## Risks and blockers

None observed for C1. The initial scratch invocation lacked the two sibling verifier dependencies required by this self-test; after copying their frozen-base versions under `/tmp`, the full requested predicate passed. No external state or production files were altered.
