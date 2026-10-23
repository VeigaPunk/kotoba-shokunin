Result: MIXED — The frozen self-test killed 18 of 26 behavioral mutants; 8 survived, and all 5 newly generated semantic equivalents survived.

# MutC1Counter — bounded mutation calibration

## Scope and observed result

- Axes: detector sensitivity, equivalent-control specificity, measurement-path relevance, exact-byte restoration.
- Isolated checkout: sandbox b1cd64bb45eee744c4ec93be8631f1eddb28fddd (/fast/scratch/hyaku/kotoba-r60/MutC1Counter). No sandbox commits were created. The lane source/index/jj state was not mutated; only this scoped report is written to the lane.
- Target: `verifiers/check_scoped_rules.py`; every variant changes one behavior-bearing line outside self_test. Frozen TARGET, rules and acceptance contract were not changed in the lane. Test-only predicate variants were restored in scratch.
- Exactly 63 detector invocations: one initial pristine run, 31 variant runs, and 31 exact-byte restored runs. Each preceding restored run is also the next variant's pristine run. No baseline/restored failure, timeout, syntax error, traceback, or inconclusive result occurred.
- Behavioral results: 18 KILLED, 8 SURVIVED, 0 INCONCLUSIVE. Equivalent controls: 0 KILLED, 5 SURVIVED. Do not mix equivalent controls into the behavioral-mutant denominator.
- The equivalent rewrites were generated in this assignment, with their semantic arguments below; they are not claimed equivalent merely because they passed.
- This is calibration of the frozen self-test, not a C1 candidate measurement or judgment. No real candidate `--rev ... --fetch` measurement was run. The self-test's own synthetic main paths remain part of the assigned detector.
- Tool installs/updates: none. No subagents, client model calls, browser, or other agent runtime were invoked.

## Detector, receipts, and byte identity

Every phase executes the same detector from the sandbox:

```sh
timeout 600 python3 -B verifiers/check_scoped_rules.py --self-test
```

The recorder invocation is `timeout 640 python3 -B probe_driver.py <ID> <mutated|restored>` (initial: `BASE pristine`), itself bounded. It unsets GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE and sets TMPDIR to `/fast/scratch/hyaku/kotoba-r60/MutC1Counter/probe-records/tmp`, so self-test temporary git repositories are also inside this seat's sandbox. The recorder only reads the target and records output; mutations/restorations were made with surgical edit operations.

Full raw receipts, stdout, stderr, UTC start, command, hashes and actual git diff are in `/fast/scratch/hyaku/kotoba-r60/MutC1Counter/probe-records/<ID>.<phase>.json`; the initial receipt is `BASE.pristine.json`. The retained recorder is `/fast/scratch/hyaku/kotoba-r60/MutC1Counter/probe_driver.py`.

Full pristine/restored SHA256 H:

`ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a`

Initial baseline (exit 0; stderr empty):

```text
counter sha256 ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a
self-test: 0 failure(s) over 318 assertions
```

Every restored receipt records `before_sha256 = after_sha256 = H`, exit 0, empty stderr and empty target diff; its stdout is exactly the initial baseline above. Each variant's before/after detector hashes are identical to the variant hash printed below. Hence each transition was H → variant hash → H; the detector never changed its own bytes.

Observed UTC interval: `2026-10-23T12:08:54.061985+00:00` to `2026-10-23T12:15:29.110552+00:00`.

Final independent command receipt:

```text
$ timeout 10 git --no-optional-locks rev-parse HEAD
b1cd64bb45eee744c4ec93be8631f1eddb28fddd
$ timeout 10 sha256sum verifiers/check_scoped_rules.py
ca2585a4a06e6e88a3d881412199fa4743f1a4553dca121f396b58d5cdb8c04a  verifiers/check_scoped_rules.py
$ timeout 10 date -u '+%Y-%m-%dT%H:%M:%SZ'
2026-10-23T12:15:45Z
```

All three commands exited 0. The revision line above identifies sandbox b1cd64bb45eee744c4ec93be8631f1eddb28fddd (/fast/scratch/hyaku/kotoba-r60/MutC1Counter), not an integration commit.

## Survivors and relevance to measurement

All effects here are [INFERENCE] from the frozen call graph; no claim is made that any survivor changes the pending build's actual F. Surviving mutants are coverage findings, not permission to change the frozen contract.

Production path: `main:2526-2528 → judge:1143-1146 → entry_row_verdict:1032,1055,1077-1096`; accepted rows then reach `main:2541 → live_why:967 → any_key_site → key_site`. Thus shared key-form/value helpers can affect both S and F, while Action/citation/SHA checks affect backing before live fetching.

| Survivor | Measurement relevance | Missing discriminator |
|---|---|---|
| M01 | Conditional false acceptance of a digit-led K; KEY_IDENT_RE is enforced at scope_key:768. | Numeric-leading key rejected, not just glob versus identifier. |
| M05 | Redundant for ordinary key sites because KEY_SUFFIX_RE still rejects an identifier suffix; NOT equivalent overall: reopen_why:992 uses key_occurrences without suffix matching and can wrongly reject a re-open. | Base row containing K only as a prefix of a longer identifier. |
| M07 | Conditional false acceptance in snapshot and live key sites. | Wildcard-bearing first token with an illegal character. |
| M10 | Conditional false rejection in snapshot and live block key sites. | A valid first nonblank list item on exactly the third following line. Existing green fixture at :1616-1617 uses the immediately following line. |
| M12 | Conditional false acceptance of a bare unmarked block glob. Existing unrelated-prose negative is still rejected by pattern_value and masks the prefix guard. | First nonblank block line is a bare glob with no list marker or quote. |
| M14 | Can change backing with multiple own-source citations; lower-priority first/last implementation-policy gap, not a demonstrated frozen-prose violation. | Different valid/invalid own-source line citations in one cell. |
| M18 | Conditional false acceptance/rejection through changed Action content sets. The existing test at :2126-2128 backticks `the`, already excluded by CONTENT_RE. | Backticked domain content that would otherwise contribute. |
| M22 | Conditional false acceptance of an incorrect full SHA pin. Full equality is mandatory even though the diagnostic displays a prefix. | A full SOURCES SHA with a correct prefix and wrong tail, keeping snapshot bytes unchanged. |

Calibration cautions: M15 is killed only through its rejection text, not a changed backing decision in the existing fixture. M16 is killed by direct threshold assertions, not an end-to-end odd-boundary witness. M19's cascading failures are dependent effects, not independent evidence. Passing the generated equivalents is evidence of non-oversensitive assertions on these rewrites only, not proof of general specificity.

## Per-variant diffs, expected detector, outputs and restoration

All path:line references below refer to the pristine frozen counter in this sandbox. The diff and stdout blocks are actual captured output, not reconstructed predictions. In raw detector diagnostics, any content/quote counts are the detector's own printed observations, not newly authored quote-count claims.

### M01 — Allow a digit-led Scope key identifier

- Point: `verifiers/check_scoped_rules.py:305`.
- Expected detector: A digit-led key must be rejected by the frozen identifier grammar; the self-test has no discriminating numeric-leading fixture.
- Verdict: **SURVIVED**. SURVIVED: contract-sensitive input-class gap. [INFERENCE] A cell naming `9paths`, with matching key-form snapshot/live evidence, can reach the backing path only under this mutant.
- Pristine receipt: `BASE.pristine.json` (exit 0, before/after H). Mutated receipt: `M01.mutated.json` (exit 0). Restored receipt: `M01.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `365da564ce36cecca39ec57cd4df33680ad524e209f694f678e0ac16e0470a85`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..f439d23 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -302,7 +302,7 @@ SOURCES_ROW_RE = re.compile(r"^\|[ \t]*S[0-9]{3,}[ \t]*\|")
 RULE_WORD_RE = re.compile(r"\b(rules?|instructions?)\b", re.IGNORECASE)
 SHA256_RE = re.compile(r"sha256[\s`*:=\[]*([0-9a-fA-F]{64})(?![0-9a-fA-F])")
 SEPARATOR_RE = re.compile(r":?-{3,}:?")
-KEY_IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
+KEY_IDENT_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
 KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*[:=]""")
 VALUE_ONLY_RE = re.compile(r"[ \t\[\|>]*")
 VALUE_STRIP = "-[\"'` \t"
```

Observed stdout (stderr empty):

```text
counter sha256 365da564ce36cecca39ec57cd4df33680ad524e209f694f678e0ac16e0470a85
self-test: 0 failure(s) over 318 assertions
```

### M02 — Drop equals-sign key forms

- Point: `verifiers/check_scoped_rules.py:306`.
- Expected detector: `key form: an equals sign is a key form` must stay true.
- Verdict: **KILLED**. KILLED by the named unit assertion.
- Pristine receipt: `M01.restored.json` (exit 0, before/after H). Mutated receipt: `M02.mutated.json` (exit 1). Restored receipt: `M02.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `41fc6579d1fb606d5cda7fd6b636240b6170f5db0d8e11f7910266acb52fec5c`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..ef94bc0 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -303,7 +303,7 @@ RULE_WORD_RE = re.compile(r"\b(rules?|instructions?)\b", re.IGNORECASE)
 SHA256_RE = re.compile(r"sha256[\s`*:=\[]*([0-9a-fA-F]{64})(?![0-9a-fA-F])")
 SEPARATOR_RE = re.compile(r":?-{3,}:?")
 KEY_IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
-KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*[:=]""")
+KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*[:]""")
 VALUE_ONLY_RE = re.compile(r"[ \t\[\|>]*")
 VALUE_STRIP = "-[\"'` \t"
 PATTERN_TOKEN_RE = re.compile(r"^[A-Za-z0-9_./*{},!-]+$")
```

Observed stdout (stderr empty):

```text
counter sha256 41fc6579d1fb606d5cda7fd6b636240b6170f5db0d8e11f7910266acb52fec5c
FAIL key form: an equals sign is a key form: got False, expected True
self-test: 1 failure(s) over 318 assertions
```

### M03 — Drop backtick closing quotes from key-form suffixes

- Point: `verifiers/check_scoped_rules.py:306`.
- Expected detector: `key form: a backticked closing before the colon is a key form` must stay true.
- Verdict: **KILLED**. KILLED by the named unit assertion.
- Pristine receipt: `M02.restored.json` (exit 0, before/after H). Mutated receipt: `M03.mutated.json` (exit 1). Restored receipt: `M03.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `9c01894c02314aede7a1af29590fad0624462a97dcca7a0ad351458a3a129ca2`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..8c60be5 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -303,7 +303,7 @@ RULE_WORD_RE = re.compile(r"\b(rules?|instructions?)\b", re.IGNORECASE)
 SHA256_RE = re.compile(r"sha256[\s`*:=\[]*([0-9a-fA-F]{64})(?![0-9a-fA-F])")
 SEPARATOR_RE = re.compile(r":?-{3,}:?")
 KEY_IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
-KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*[:=]""")
+KEY_SUFFIX_RE = re.compile(r"""["']?[ \t]*[:=]""")
 VALUE_ONLY_RE = re.compile(r"[ \t\[\|>]*")
 VALUE_STRIP = "-[\"'` \t"
 PATTERN_TOKEN_RE = re.compile(r"^[A-Za-z0-9_./*{},!-]+$")
```

Observed stdout (stderr empty):

```text
counter sha256 9c01894c02314aede7a1af29590fad0624462a97dcca7a0ad351458a3a129ca2
FAIL key form: a backticked closing before the colon is a key form: got False, expected True
self-test: 1 failure(s) over 318 assertions
```

### M04 — Remove the left identifier boundary

- Point: `verifiers/check_scoped_rules.py:807`.
- Expected detector: `key form: a key inside a longer identifier fails` and the judge fixture for `xpaths` must reject.
- Verdict: **KILLED**. KILLED at both helper and judge levels.
- Pristine receipt: `M03.restored.json` (exit 0, before/after H). Mutated receipt: `M04.mutated.json` (exit 1). Restored receipt: `M04.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `d218a32b4affb495f89d9db62814706468012652e1e7a9cfd5ddc2911fa3755f`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..a945bb0 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -804,7 +804,7 @@ def key_occurrences(line: str, key: str) -> list[tuple[int, int]]:
         if i < 0:
             return out
         j = i + len(key)
-        left_ok = i == 0 or line[i - 1] not in IDENT
+        left_ok = True
         right_ok = j >= len(line) or line[j] not in IDENT
         if left_ok and right_ok:
             out.append((i, j))
```

Observed stdout (stderr empty):

```text
counter sha256 d218a32b4affb495f89d9db62814706468012652e1e7a9cfd5ddc2911fa3755f
FAIL key form: a key inside a longer identifier fails: got True, expected False
FAIL a key only inside a longer identifier drops the row: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
self-test: 2 failure(s) over 318 assertions
```

### M05 — Remove the right identifier boundary

- Point: `verifiers/check_scoped_rules.py:808`.
- Expected detector: The boundary helper must not treat `pathsExtra` as the key `paths`; an E1 re-open fixture must accept that non-key occurrence.
- Verdict: **SURVIVED**. SURVIVED: the key-site suffix regex masks this mutation for ordinary key sites, but E1 calls key_occurrences directly. [INFERENCE] A base row mentioning `pathsExtra` would wrongly block a re-open for `paths`. This is a conditional false-negative gap, not a demonstrated current measurement change.
- Pristine receipt: `M04.restored.json` (exit 0, before/after H). Mutated receipt: `M05.mutated.json` (exit 0). Restored receipt: `M05.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `24b7b7e26234e07debad552436d0bc4c653e8d2a7b44238d8771b529e9f96bcb`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..4b4cb2d 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -805,7 +805,7 @@ def key_occurrences(line: str, key: str) -> list[tuple[int, int]]:
             return out
         j = i + len(key)
         left_ok = i == 0 or line[i - 1] not in IDENT
-        right_ok = j >= len(line) or line[j] not in IDENT
+        right_ok = True
         if left_ok and right_ok:
             out.append((i, j))
         start = i + 1
```

Observed stdout (stderr empty):

```text
counter sha256 24b7b7e26234e07debad552436d0bc4c653e8d2a7b44238d8771b529e9f96bcb
self-test: 0 failure(s) over 318 assertions
```

### M06 — Search the whole value for a wildcard instead of its first token

- Point: `verifiers/check_scoped_rules.py:830`.
- Expected detector: `value: a sentence that mentions a pattern is not` and description-sentence judge fixtures must reject.
- Verdict: **KILLED**. KILLED at helper, key-site and judge levels.
- Pristine receipt: `M05.restored.json` (exit 0, before/after H). Mutated receipt: `M06.mutated.json` (exit 1). Restored receipt: `M06.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `119c0718c7c3c6797b447e7a9b69b56af1e152fd18cff536525976dc21ac4bf8`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..5536bec 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -827,7 +827,7 @@ def pattern_value(text: str) -> bool:
 
     It must contain `*` and consist only of `[A-Za-z0-9_./*{},!-]`."""
     tok = first_value_token(text)
-    return "*" in tok and PATTERN_TOKEN_RE.match(tok) is not None
+    return "*" in text and PATTERN_TOKEN_RE.match(tok) is not None
 
 
 def block_only(rest: str) -> bool:
```

Observed stdout (stderr empty):

```text
counter sha256 119c0718c7c3c6797b447e7a9b69b56af1e152fd18cff536525976dc21ac4bf8
FAIL value: a sentence that mentions a pattern is not: got True, expected False
FAIL key form: an assigned sentence mentioning a pattern fails: got True, expected False
FAIL a description whose value mentions a pattern still fails: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
self-test: 3 failure(s) over 318 assertions
```

### M07 — Drop the glob-token alphabet guard

- Point: `verifiers/check_scoped_rules.py:830`.
- Expected detector: A first token such as `src/*.ts?` must fail the pinned pattern-token alphabet; no existing fixture discriminates this guard.
- Verdict: **SURVIVED**. SURVIVED: conditional false-positive gap in both snapshot and live key sites. [INFERENCE] The mutant accepts a wildcard token containing a disallowed `?`, provided other row checks pass.
- Pristine receipt: `M06.restored.json` (exit 0, before/after H). Mutated receipt: `M07.mutated.json` (exit 0). Restored receipt: `M07.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `788c073cee046aa2d714ec3ef3c3fff9ef0106a8afdae51871378484be870f10`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..f38fb64 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -827,7 +827,7 @@ def pattern_value(text: str) -> bool:
 
     It must contain `*` and consist only of `[A-Za-z0-9_./*{},!-]`."""
     tok = first_value_token(text)
-    return "*" in tok and PATTERN_TOKEN_RE.match(tok) is not None
+    return "*" in tok
 
 
 def block_only(rest: str) -> bool:
```

Observed stdout (stderr empty):

```text
counter sha256 788c073cee046aa2d714ec3ef3c3fff9ef0106a8afdae51871378484be870f10
self-test: 0 failure(s) over 318 assertions
```

### M08 — Drop the mandatory wildcard test

- Point: `verifiers/check_scoped_rules.py:830`.
- Expected detector: No-pattern key sites must fail; the live-key failure fixture must reduce F without reducing S.
- Verdict: **KILLED**. KILLED at helper, judge and end-to-end main levels.
- Pristine receipt: `M07.restored.json` (exit 0, before/after H). Mutated receipt: `M08.mutated.json` (exit 1). Restored receipt: `M08.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `454afb783b66cd9d547f69d869311b547ce10c8d11110adf220edc23f8b690ed`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..3da817b 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -827,7 +827,7 @@ def pattern_value(text: str) -> bool:
 
     It must contain `*` and consist only of `[A-Za-z0-9_./*{},!-]`."""
     tok = first_value_token(text)
-    return "*" in tok and PATTERN_TOKEN_RE.match(tok) is not None
+    return PATTERN_TOKEN_RE.match(tok) is not None
 
 
 def block_only(rest: str) -> bool:
```

Observed stdout (stderr empty):

```text
counter sha256 454afb783b66cd9d547f69d869311b547ce10c8d11110adf220edc23f8b690ed
FAIL value: a sentence that mentions a pattern is not: got True, expected False
FAIL key form: description at a line with no pattern fails: got True, expected False
FAIL key form: an assigned sentence mentioning a pattern fails: got True, expected False
FAIL any key site: a page without the key is not found: got True, expected False
FAIL a scope key on a line with no pattern drops the row: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL the no-pattern key is reported with its key and line: got False, expected True
FAIL a description whose value mentions a pattern still fails: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL main: a live page without the key site drops F, not S: got (0, 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4'), expected (1, 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 3 of 4')
FAIL main: the live key failure is named: got False, expected True
self-test: 9 failure(s) over 318 assertions
```

### M09 — Stop treating comma as a first-token delimiter

- Point: `verifiers/check_scoped_rules.py:317`.
- Expected detector: `value: the token stops at a comma` must return the token without its comma.
- Verdict: **KILLED**. KILLED by the exact first-token unit assertion.
- Pristine receipt: `M08.restored.json` (exit 0, before/after H). Mutated receipt: `M09.mutated.json` (exit 1). Restored receipt: `M09.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `2276fde5b2379aac4dd436a4a8b70fe96abee1cf56070bf47d213813e9879ab7`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..da313a5 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -314,7 +314,7 @@ CITE_RE = re.compile(r"(S\d{3,})\s*:\s*(\d+)")
 REOPEN_RE = re.compile(r"^re-opens\s+(S\d{3,})\s*(?:\u2014|\u2013|--|-)")
 CONTENT_RE = re.compile(r"[a-z]{4,}")
 IDENT = frozenset(string.ascii_letters + string.digits + "_")
-TOKEN_CUT = frozenset(" \t\r\v\f,\"'`])}>")
+TOKEN_CUT = frozenset(" \t\r\v\f\"'`])}>")
 BOUNDARY_PREV = frozenset(" \t\r\n`\"'([")
 TRIM_CHARS = ".,;:!?)]}'\""
 ASCII_ALNUM = frozenset(string.ascii_letters + string.digits)
```

Observed stdout (stderr empty):

```text
counter sha256 2276fde5b2379aac4dd436a4a8b70fe96abee1cf56070bf47d213813e9879ab7
FAIL value: the token stops at a comma: got 'a/*.ts,', expected 'a/*.ts'
self-test: 1 failure(s) over 318 assertions
```

### M10 — Shorten block lookahead from the next three lines to two

- Point: `verifiers/check_scoped_rules.py:846`.
- Expected detector: A block with its first nonblank list value exactly on the third following line must pass; that boundary-green fixture is absent.
- Verdict: **SURVIVED**. SURVIVED: conditional false-negative gap in snapshot and live checks. [INFERENCE] `["paths:", "", "", "  - \"src/*.ts\""]` is inside the frozen window but outside the mutant window.
- Pristine receipt: `M09.restored.json` (exit 0, before/after H). Mutated receipt: `M10.mutated.json` (exit 0). Restored receipt: `M10.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `069eeb51861e711ef27b8e2fc71c7e1840b64d5ec63e89fb7a36fc66ac2ee703`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..e430f06 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -843,7 +843,7 @@ def value_after(lines: list[str], L: int, rest: str) -> str | None:
     with `-` or a quote; any other first nonblank line leaves no value."""
     if not block_only(rest):
         return rest
-    for line in lines[L:L + 3]:
+    for line in lines[L:L + 2]:
         if not line.strip():
             continue
         return line if line.lstrip().startswith(("-", '"', "'", "`")) else None
```

Observed stdout (stderr empty):

```text
counter sha256 069eeb51861e711ef27b8e2fc71c7e1840b64d5ec63e89fb7a36fc66ac2ee703
self-test: 0 failure(s) over 318 assertions
```

### M11 — Enlarge block lookahead to the next four lines

- Point: `verifiers/check_scoped_rules.py:846`.
- Expected detector: `key form: a block value four lines down fails` must stay false.
- Verdict: **KILLED**. KILLED by the window upper-bound helper assertion.
- Pristine receipt: `M10.restored.json` (exit 0, before/after H). Mutated receipt: `M11.mutated.json` (exit 1). Restored receipt: `M11.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `3b23b6867d841a8ca4bf314c5e66062fcf3e3dfd07adb664fcd3e0099bcee54b`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..c6bec58 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -843,7 +843,7 @@ def value_after(lines: list[str], L: int, rest: str) -> str | None:
     with `-` or a quote; any other first nonblank line leaves no value."""
     if not block_only(rest):
         return rest
-    for line in lines[L:L + 3]:
+    for line in lines[L:L + 4]:
         if not line.strip():
             continue
         return line if line.lstrip().startswith(("-", '"', "'", "`")) else None
```

Observed stdout (stderr empty):

```text
counter sha256 3b23b6867d841a8ca4bf314c5e66062fcf3e3dfd07adb664fcd3e0099bcee54b
FAIL key form: a block value four lines down fails: got True, expected False
self-test: 1 failure(s) over 318 assertions
```

### M12 — Drop the block list-item/quote prefix guard

- Point: `verifiers/check_scoped_rules.py:849`.
- Expected detector: An unmarked first nonblank block line containing a bare glob must fail; the existing unrelated-prose negative still fails for its non-glob token.
- Verdict: **SURVIVED**. SURVIVED: conditional false-positive gap in snapshot and live checks. [INFERENCE] `paths:` followed by bare `src/*.ts` would now pass without the required list marker or quote.
- Pristine receipt: `M11.restored.json` (exit 0, before/after H). Mutated receipt: `M12.mutated.json` (exit 0). Restored receipt: `M12.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `79afde2dfa723995b18f93834ea07a02cd555db237b95783340c21b5d5a418d9`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..a766a4f 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -846,7 +846,7 @@ def value_after(lines: list[str], L: int, rest: str) -> str | None:
     for line in lines[L:L + 3]:
         if not line.strip():
             continue
-        return line if line.lstrip().startswith(("-", '"', "'", "`")) else None
+        return line
     return None
```

Observed stdout (stderr empty):

```text
counter sha256 79afde2dfa723995b18f93834ea07a02cd555db237b95783340c21b5d5a418d9
self-test: 0 failure(s) over 318 assertions
```

### M13 — Accept a citation belonging to any source id

- Point: `verifiers/check_scoped_rules.py:783`.
- Expected detector: `citation: another row's id is a named failure`, scope-source mismatch and action-source mismatch fixtures must reject.
- Verdict: **KILLED**. KILLED at citation helper and judge levels.
- Pristine receipt: `M12.restored.json` (exit 0, before/after H). Mutated receipt: `M13.mutated.json` (exit 1). Restored receipt: `M13.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `c2f1db102fe85705ad9c5c0c755b44e1110ba6195f1dfe5a949360f416546fb5`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..8f2c861 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -780,7 +780,7 @@ def citation_why(cell: str, sid: str | None, what: str) -> tuple[int | None, lis
     """The line L a cell cites for its OWN source row, or the reason it does not."""
     cites = citations(cell)
     if sid:
-        own = [n for s, n in cites if s == sid]
+        own = [n for s, n in cites]
         if own:
             return own[0], []
         if cites:
```

Observed stdout (stderr empty):

```text
counter sha256 c2f1db102fe85705ad9c5c0c755b44e1110ba6195f1dfe5a949360f416546fb5
FAIL citation: another row's id is a named failure: got (5, []), expected (None, ["SKILL.md scope key cell cites S901 :5, not the row's own source S900"])
FAIL a scope key citing another row's source is not backed: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL an action citing another row's source is not backed: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
self-test: 3 failure(s) over 318 assertions
```

### M14 — Select the last own-source citation instead of the first

- Point: `verifiers/check_scoped_rules.py:785`.
- Expected detector: A fixture with distinct first/last own-source line citations would distinguish the implementation policy; current fixtures do not.
- Verdict: **SURVIVED**. SURVIVED: lower-priority implementation-selection gap. [INFERENCE] Multiple own-source citations can select a different scope/action line and change backing. The frozen prose does not explicitly choose first versus last citation, so this survivor alone is not evidence of a frozen-contract violation.
- Pristine receipt: `M13.restored.json` (exit 0, before/after H). Mutated receipt: `M14.mutated.json` (exit 0). Restored receipt: `M14.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `4e2745dd05e2c749ec386b5a330ab7f244e92419cba014b20051da742deb308b`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..e4ab40d 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -782,7 +782,7 @@ def citation_why(cell: str, sid: str | None, what: str) -> tuple[int | None, lis
     if sid:
         own = [n for s, n in cites if s == sid]
         if own:
-            return own[0], []
+            return own[-1], []
         if cites:
             return None, ["%s cites %s, not the row's own source %s"
                           % (what, ", ".join("%s :%d" % c for c in cites), sid)]
```

Observed stdout (stderr empty):

```text
counter sha256 4e2745dd05e2c749ec386b5a330ab7f244e92419cba014b20051da742deb308b
self-test: 0 failure(s) over 318 assertions
```

### M15 — Lower the Action content floor

- Point: `verifiers/check_scoped_rules.py:252`.
- Expected detector: `the thin action is reported with its count` must retain its original rejection diagnostic.
- Verdict: **KILLED**. KILLED ONLY by a diagnostic assertion: the existing thin-action fixture remains unbacked through insufficient overlap. This run does not demonstrate decision-level sensitivity to the content floor.
- Pristine receipt: `M14.restored.json` (exit 0, before/after H). Mutated receipt: `M15.mutated.json` (exit 1). Restored receipt: `M15.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `52946fa040e1b4a97c3f1f4169c3f35fd41f79352449c89dce738f7eee0e3288`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..9ee228e 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -249,7 +249,7 @@ SNAPSHOT_DIR = ".ufo/waves/round-60/snapshots"
 TARGET = 3
 MIN_WORDS = 6
 MAX_WORDS = 25
-MIN_CONTENT = 3
+MIN_CONTENT = 2
 MIN_SHARED = 2
 OPENED = ("2026-10-23",)
 MAX_BYTES = 5 * 1024 * 1024
```

Observed stdout (stderr empty):

```text
counter sha256 52946fa040e1b4a97c3f1f4169c3f35fd41f79352449c89dce738f7eee0e3288
FAIL the thin action is reported with its count: got False, expected True
self-test: 1 failure(s) over 318 assertions
```

### M16 — Round the half-overlap threshold down

- Point: `verifiers/check_scoped_rules.py:891`.
- Expected detector: The odd-size action_need assertions must retain the ceiling threshold.
- Verdict: **KILLED**. KILLED by direct action_need assertions; the output does not show a changed end-to-end decision.
- Pristine receipt: `M15.restored.json` (exit 0, before/after H). Mutated receipt: `M16.mutated.json` (exit 1). Restored receipt: `M16.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `b2950714060d904e6ddfaf758336e5cfdc048ec870c5acfcbe99ed442efec52b`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..cd56550 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -888,7 +888,7 @@ def content_words(text: str) -> set[str]:
 
 def action_need(n_content: int) -> int:
     """The Action conjunct's threshold: max(2, ceil(|W| / 2))."""
-    return max(MIN_SHARED, (n_content + 1) // 2)
+    return max(MIN_SHARED, n_content // 2)
 
 
 def action_conjunct(lines: list[str], cell: str, L: int | None) -> list[str]:
```

Observed stdout (stderr empty):

```text
counter sha256 b2950714060d904e6ddfaf758336e5cfdc048ec870c5acfcbe99ed442efec52b
FAIL action need: 5 content words need 3: got 2, expected 3
FAIL action need: 7 content words need 4: got 3, expected 4
self-test: 2 failure(s) over 318 assertions
```

### M17 — Use union instead of intersection for shared action words

- Point: `verifiers/check_scoped_rules.py:908`.
- Expected detector: The one-shared-word and longer-action shortfall fixtures must reject.
- Verdict: **KILLED**. KILLED at Action helper and judge levels.
- Pristine receipt: `M16.restored.json` (exit 0, before/after H). Mutated receipt: `M17.mutated.json` (exit 1). Restored receipt: `M17.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `721f7bb563ea62b0de1faf4984ece3dbe85d411cf75305ecb3b94e022f3b0c37`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..9e4639b 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -905,7 +905,7 @@ def action_conjunct(lines: list[str], cell: str, L: int | None) -> list[str]:
         return ["action cell holds %d distinct content word(s) (need >= %d)"
                 % (len(w), MIN_CONTENT)]
     need = action_need(len(w))
-    shared = w & content_words(lines[L - 1])
+    shared = w | content_words(lines[L - 1])
     if len(shared) < need:
         return ["action cell shares %d of its %d content word(s) with line %d "
                 "(need >= %d)" % (len(shared), len(w), L, need)]
```

Observed stdout (stderr empty):

```text
counter sha256 721f7bb563ea62b0de1faf4984ece3dbe85d411cf75305ecb3b94e022f3b0c37
FAIL an action sharing one content word is not backed: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL the action shortfall is reported with its counts: got False, expected True
FAIL a longer action needs half of its words, not two: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL the half threshold is reported with its counts: got False, expected True
FAIL action: one shared word fails: got [], expected ['action cell shares 1 of its 4 content word(s) with line 1 (need >= 2)']
self-test: 5 failure(s) over 318 assertions
```

### M18 — Count text inside backticks as Action content

- Point: `verifiers/check_scoped_rules.py:884`.
- Expected detector: Backticked content must not contribute; the existing exclusion fixture backticks `the`, which CONTENT_RE already excludes.
- Verdict: **SURVIVED**. SURVIVED: meaningful content-accounting gap on the backing path. [INFERENCE] Backticked domain terms can alter the minimum, threshold, or shared set. This can produce false positives or false negatives depending on the row.
- Pristine receipt: `M17.restored.json` (exit 0, before/after H). Mutated receipt: `M18.mutated.json` (exit 0). Restored receipt: `M18.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `5a5d344b44abd5f3796ed3f591431a7eaffc217554bbf59a0704c4809939949c`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..9a8fe2e 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -881,7 +881,7 @@ def any_key_site(text: str, key: str | None) -> bool:
 def content_words(text: str) -> set[str]:
     """The cell's content words: lowercase `[a-z]{4,}` runs outside backticks
     and `S### :L` citations, minus the pinned STOPWORDS."""
-    t = BACKTICK_RE.sub(" ", text)
+    t = text
     t = CITE_RE.sub(" ", t)
     return {w for w in CONTENT_RE.findall(t.lower()) if w not in STOPWORDS}
```

Observed stdout (stderr empty):

```text
counter sha256 5a5d344b44abd5f3796ed3f591431a7eaffc217554bbf59a0704c4809939949c
self-test: 0 failure(s) over 318 assertions
```

### M19 — Misclassify domain word scope as a stopword

- Point: `verifiers/check_scoped_rules.py:341`.
- Expected detector: `action: content words drop backticks, citations and stopwords` and uppercase-content assertions must retain `scope`.
- Verdict: **KILLED**. KILLED, with cascading judge/main failures. The many failures are dependent effects of one mutation, not independent coverage claims.
- Pristine receipt: `M18.restored.json` (exit 0, before/after H). Mutated receipt: `M19.mutated.json` (exit 1). Restored receipt: `M19.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `00d3671408fd02140492ac07f975c71c60120dcfb1e2858fd0f8800c3afaf7e8`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..9781db1 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -338,7 +338,7 @@ STOPWORDS = frozenset((
     "that", "their", "them", "then", "there", "these", "they", "this",
     "those", "through", "thus", "under", "until", "upon", "very", "what",
     "when", "where", "whether", "which", "while", "will", "with", "within",
-    "without", "would", "your", "yours",
+    "without", "would", "your", "yours", "scope",
 ))
```

Observed stdout (stderr empty):

```text
counter sha256 00d3671408fd02140492ac07f975c71c60120dcfb1e2858fd0f8800c3afaf7e8
FAIL the synthetic world backs all four clients: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL E5 dropped: two rows may share a token and both back: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL the scope key and key line are carried on the report: got [('paths', 5), ('globs', 4)], expected [('paths', 5), ('applyTo', 4), ('applyTo', 4), ('globs', 4)]
FAIL a duplicate SKILL.md row disqualifies the client: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a second entry row does not disqualify a good one: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL no entry row for the client is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL an S### already at base is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a base URL is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a base URL reached by a path-case alias is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a tier B row is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a queued row is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL another opened date is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a non-docs kind is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL an off-host URL is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a tracker URL on a pinned host is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a changelog URL is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a source cell without a URL is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a malformed rule token is not backed and leaves K: got (['Claude Code'], 3), expected (['Claude Code', 'VS Code', 'Copilot CLI'], 3)
FAIL a hook token is not well-formed (A1 NOT-words): got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a rule cell without a backticked token is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL a token carrying another client's marker is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL a quote without the token is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL a quote without a rule word outside the token is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL a quote whose only rule word is inside the token is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a quote whose token differs only in case is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL a two-word quote is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL a 26-word quote is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL an entry source cell that is not one S### id is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL an S### absent from SOURCES.md is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL a quote missing from the Gate is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL E4: an entry Rule files cell that differs from SKILL.md is not backed: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL E4: a backticked Rule files cell still backs: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL E4: the raw ./ form in the cell still backs: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL E4: the normalised form is not the raw cell of a ./ token: got ['Claude Code'], expected ['Claude Code', 'VS Code', 'Copilot CLI']
FAIL a missing snapshot is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a snapshot whose sha256 differs is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a SOURCES row without a full 64-hex sha256 is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a snapshot that does not carry the quote is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a scope key on a line with no pattern drops the row: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a description whose value mentions a pattern still fails: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL the Cursor table-cell line is not a key form for description: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL the Cursor table-cell line is not a key form for alwaysApply: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a key only inside a longer identifier drops the row: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL an off-by-one citation to a line without the key drops the row: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a block value two lines down backs in the judge: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a block value four lines down drops the row: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a scope key citing another row's source is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a scope key with no citation is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL an action citing another row's source is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL an action with no citation is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL an action on a citation line out of range is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL an action sharing one content word is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL an action with two content words is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a longer action needs half of its words, not two: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL action: two shared words pass: got ['action cell shares 1 of its 3 content word(s) with line 1 (need >= 2)'], expected []
FAIL action: content words drop backticks, citations and stopwords: got {'rule', 'file'}, expected {'scope', 'rule', 'file'}
FAIL action: an uppercase word is compared lowercased: got {'rule'}, expected {'scope', 'rule'}
FAIL v2: a base URL re-opened by its base id backs: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL v2: base URLs without the re-open prefix are not backed: got [], expected ['VS Code', 'Copilot CLI']
FAIL v2: the re-open prefix is a prefix, not a mention mid-cell: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL v2: a re-open naming a base row whose URL differs is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL v2: a re-open whose base row line already holds K is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL v2: a re-open naming a non-base id is not backed: got ['Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL v2: a plain hyphen is the same re-open separator: got ['Claude Code', 'Gemini CLI'], expected ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL main: the satisfying world exits 0: got 1, expected 0
FAIL main: the exact summary line is the first line: got 'scoped rule files backed on committed snapshots 2 of 4; found on the live page 2 of 4', expected 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4'
FAIL main: no reject line for a found row: got ['reject VS Code: entry row S902: snapshot .ufo/waves/round-60/snapshots/S902.page: action cell holds 2 distinct content word(s) (need >= 3)', 'reject Copilot CLI: entry row S903: snapshot .ufo/waves/round-60/snapshots/S903.page: action cell holds 2 distinct content word(s) (need >= 3)'], expected []
FAIL main: a divergent working tree does not substitute (M09): got (1, 'scoped rule files backed on committed snapshots 2 of 4; found on the live page 2 of 4'), expected (0, 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4')
FAIL main: a live page without the key site drops F, not S: got (1, 'scoped rule files backed on committed snapshots 2 of 4; found on the live page 1 of 4'), expected (1, 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 3 of 4')
FAIL main: the same 3 of 4 meets a target of 3: got 1, expected 0
FAIL main: an HTTP 404 keeps S at 4 and F at 0: got 'scoped rule files backed on committed snapshots 2 of 4; found on the live page 0 of 4', expected 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 0 of 4'
FAIL a curl failure keeps S at 4 and F at 0: got 'scoped rule files backed on committed snapshots 2 of 4; found on the live page 0 of 4', expected 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 0 of 4'
FAIL a curl failure names the backed rows: got (True, False), expected (True, True)
FAIL the unfrozen sentinel still prints the summary: got 'scoped rule files backed on committed snapshots 2 of 4; found on the live page 2 of 4', expected 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4'
FAIL without --fetch the summary reads 'live not run': got 'scoped rule files backed on committed snapshots 2 of 4; live not run', expected 'scoped rule files backed on committed snapshots 4 of 4; live not run'
FAIL without --fetch a backed row is not rejected: got ['reject VS Code: entry row S902: snapshot .ufo/waves/round-60/snapshots/S902.page: action cell holds 2 distinct content word(s) (need >= 3)', 'reject Copilot CLI: entry row S903: snapshot .ufo/waves/round-60/snapshots/S903.page: action cell holds 2 distinct content word(s) (need >= 3)'], expected []
FAIL the broken world prints the three-of-four line: got 'scoped rule files backed on committed snapshots 1 of 4; found on the live page 1 of 4', expected 'scoped rule files backed on committed snapshots 3 of 4; found on the live page 3 of 4'
FAIL v2 main: 3 of 3 found with 2 re-opens exits 0: got 1, expected 0
FAIL v2 main: the exact summary line names 3 of 3: got 'scoped rule files backed on committed snapshots 2 of 3; found on the live page 2 of 3', expected 'scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3'
FAIL v2 main: no reject line for the three measured clients: got ['reject VS Code: entry row S902: snapshot .ufo/waves/round-60/snapshots/S902.page: action cell holds 2 distinct content word(s) (need >= 3)'], expected []
self-test: 80 failure(s) over 318 assertions
```

### M20 — Remove with from STOPWORDS

- Point: `verifiers/check_scoped_rules.py:340`.
- Expected detector: `action: content words drop backticks, citations and stopwords` must still drop `with`.
- Verdict: **KILLED**. KILLED by direct content-accounting and Action helper assertions.
- Pristine receipt: `M19.restored.json` (exit 0, before/after H). Mutated receipt: `M20.mutated.json` (exit 1). Restored receipt: `M20.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `2e52df5b18e4d537b115cbfc1293e4b9cf700b70e996ac7af7c6967db21d2488`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..76406f6 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -337,7 +337,7 @@ STOPWORDS = frozenset((
     "over", "same", "shall", "should", "since", "some", "such", "than",
     "that", "their", "them", "then", "there", "these", "they", "this",
     "those", "through", "thus", "under", "until", "upon", "very", "what",
-    "when", "where", "whether", "which", "while", "will", "with", "within",
+    "when", "where", "whether", "which", "while", "will", "within",
     "without", "would", "your", "yours",
 ))
```

Observed stdout (stderr empty):

```text
counter sha256 2e52df5b18e4d537b115cbfc1293e4b9cf700b70e996ac7af7c6967db21d2488
FAIL action: two shared words pass: got ['action cell shares 2 of its 5 content word(s) with line 1 (need >= 3)'], expected []
FAIL action: content words drop backticks, citations and stopwords: got {'scope', 'with', 'rule', 'file'}, expected {'scope', 'file', 'rule'}
self-test: 2 failure(s) over 318 assertions
```

### M21 — Disable snapshot sha256 mismatch rejection

- Point: `verifiers/check_scoped_rules.py:1078`.
- Expected detector: `a snapshot whose sha256 differs is not backed` and its named mismatch diagnostic must reject.
- Verdict: **KILLED**. KILLED at judge level.
- Pristine receipt: `M20.restored.json` (exit 0, before/after H). Mutated receipt: `M21.mutated.json` (exit 1). Restored receipt: `M21.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `b59907075cf0c8f4c449c74a4614d88dee87701ce02111a67e98c27d6ba4f92e`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..b1e253b 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -1075,7 +1075,7 @@ def entry_row_verdict(er: list[str], client: str, token: str | None,
                                % snapshot_path(sid))
                 else:
                     got = hashlib.sha256(data).hexdigest()
-                    if got != sha:
+                    if False:
                         why.append("snapshot %s sha256 %s... does not equal the "
                                    "SOURCES row sha256 %s..."
                                    % (snapshot_path(sid), got[:12], sha[:12]))
```

Observed stdout (stderr empty):

```text
counter sha256 b59907075cf0c8f4c449c74a4614d88dee87701ce02111a67e98c27d6ba4f92e
FAIL a snapshot whose sha256 differs is not backed: got ['Claude Code', 'VS Code', 'Copilot CLI', 'Gemini CLI'], expected ['VS Code', 'Copilot CLI', 'Gemini CLI']
FAIL a snapshot sha mismatch is reported as such: got False, expected True
self-test: 2 failure(s) over 318 assertions
```

### M22 — Compare only the first twelve sha256 hex digits

- Point: `verifiers/check_scoped_rules.py:1078`.
- Expected detector: A SOURCES digest with the true prefix but an incorrect tail must fail full-pin equality; the existing changed-snapshot fixture does not isolate tail comparison.
- Verdict: **SURVIVED**. SURVIVED: meaningful snapshot-pin gap on every backing path. [INFERENCE] Altering only the SOURCES digest tail while preserving its prefix would pass this mutant. No hash collision is needed to construct that missing fixture.
- Pristine receipt: `M21.restored.json` (exit 0, before/after H). Mutated receipt: `M22.mutated.json` (exit 0). Restored receipt: `M22.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `0698d8a9b1d75fdf3e0dc379587f303730327b011ce9fb7f29855e9d4dbeaa42`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..34c19f7 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -1075,7 +1075,7 @@ def entry_row_verdict(er: list[str], client: str, token: str | None,
                                % snapshot_path(sid))
                 else:
                     got = hashlib.sha256(data).hexdigest()
-                    if got != sha:
+                    if got[:12] != sha[:12]:
                         why.append("snapshot %s sha256 %s... does not equal the "
                                    "SOURCES row sha256 %s..."
                                    % (snapshot_path(sid), got[:12], sha[:12]))
```

Observed stdout (stderr empty):

```text
counter sha256 0698d8a9b1d75fdf3e0dc379587f303730327b011ce9fb7f29855e9d4dbeaa42
self-test: 0 failure(s) over 318 assertions
```

### M23 — Disable the live key-site requirement

- Point: `verifiers/check_scoped_rules.py:967`.
- Expected detector: `main: a live page without the key site drops F, not S` and its named live failure must hold.
- Verdict: **KILLED**. KILLED on the successful/failing end-to-end main path.
- Pristine receipt: `M22.restored.json` (exit 0, before/after H). Mutated receipt: `M23.mutated.json` (exit 1). Restored receipt: `M23.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `0e2712f1e05b6f6a35a98b8bcd6c04dbe04c1846e3bf462df9dfa47464fc18f3`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..aaa3951 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -964,7 +964,7 @@ def quote_why(page_text: str, quote: str) -> list[str]:
 def live_why(page_text: str, quote: str, key: str | None) -> list[str]:
     """Why the live page does not carry the quote and a key-form site for K."""
     why = quote_why(page_text, quote)
-    if key and not any_key_site(page_text, key):
+    if False:
         why.append("no key-form site for %r on the page" % key)
     return why
```

Observed stdout (stderr empty):

```text
counter sha256 0e2712f1e05b6f6a35a98b8bcd6c04dbe04c1846e3bf462df9dfa47464fc18f3
FAIL main: a live page without the key site drops F, not S: got (0, 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4'), expected (1, 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 3 of 4')
FAIL main: the live key failure is named: got False, expected True
self-test: 2 failure(s) over 318 assertions
```

### M24 — Skip the final line in live key-site scanning

- Point: `verifiers/check_scoped_rules.py:875`.
- Expected detector: `any key site: a later line is found` must find the terminal key line.
- Verdict: **KILLED**. KILLED by the terminal-line helper assertion.
- Pristine receipt: `M23.restored.json` (exit 0, before/after H). Mutated receipt: `M24.mutated.json` (exit 1). Restored receipt: `M24.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `700fb81300e213c2edd465167298be48dafe1142df2e83f77ee00426d5b50c36`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..2c8ec15 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -872,7 +872,7 @@ def key_site(lines: list[str], L: int, key: str | None) -> bool:
 def any_key_site(text: str, key: str | None) -> bool:
     """A key-form site for `key` at any line of the page (the live-page check)."""
     lines = text.splitlines()
-    for n in range(1, len(lines) + 1):
+    for n in range(1, len(lines)):
         if key_site(lines, n, key):
             return True
     return False
```

Observed stdout (stderr empty):

```text
counter sha256 700fb81300e213c2edd465167298be48dafe1142df2e83f77ee00426d5b50c36
FAIL any key site: a later line is found: got False, expected True
self-test: 1 failure(s) over 318 assertions
```

### M25 — Make the predicate reject equality with TARGET

- Point: `verifiers/check_scoped_rules.py:1249`.
- Expected detector: `predicate: fetch, 3 found, passes` and the main target-boundary fixtures must exit zero.
- Verdict: **KILLED**. KILLED at predicate and end-to-end main levels.
- Pristine receipt: `M24.restored.json` (exit 0, before/after H). Mutated receipt: `M25.mutated.json` (exit 1). Restored receipt: `M25.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `bcb0733c9553441f3a01dcf391602b1358273acfefdf2e7d36c63ab276f09d77`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..8dcd7e0 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -1246,7 +1246,7 @@ def predicate(fetching: bool, found: int) -> int:
     """Exit 0 iff fetching, the target is frozen and F >= TARGET."""
     if not fetching or TARGET is None:
         return 1
-    return 0 if found >= TARGET else 1
+    return 0 if found > TARGET else 1
 
 
 def _outcome(fn) -> tuple[str, object]:
```

Observed stdout (stderr empty):

```text
counter sha256 bcb0733c9553441f3a01dcf391602b1358273acfefdf2e7d36c63ab276f09d77
FAIL predicate: fetch, 3 found, passes: got 1, expected 0
FAIL main: the satisfying world exits 0: got 1, expected 0
FAIL main: a divergent working tree does not substitute (M09): got (1, 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4'), expected (0, 'scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4')
FAIL main: the same 3 of 4 meets a target of 3: got 1, expected 0
FAIL v2 main: 3 of 3 found with 2 re-opens exits 0: got 1, expected 0
self-test: 5 failure(s) over 318 assertions
```

### M26 — Remove the predicate fetching gate

- Point: `verifiers/check_scoped_rules.py:1247`.
- Expected detector: `predicate: no fetch always fails` must return failure even when found exceeds TARGET.
- Verdict: **KILLED**. KILLED by the direct predicate assertion.
- Pristine receipt: `M25.restored.json` (exit 0, before/after H). Mutated receipt: `M26.mutated.json` (exit 1). Restored receipt: `M26.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `f746ccfbe8c8280aefdca3e6c6f22c0c702eb9e8c66e8020676cf8f719e2e97b`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..1ee06e0 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -1244,7 +1244,7 @@ def reject_line(client: str, why: list[str]) -> str:
 
 def predicate(fetching: bool, found: int) -> int:
     """Exit 0 iff fetching, the target is frozen and F >= TARGET."""
-    if not fetching or TARGET is None:
+    if TARGET is None:
         return 1
     return 0 if found >= TARGET else 1
```

Observed stdout (stderr empty):

```text
counter sha256 f746ccfbe8c8280aefdca3e6c6f22c0c702eb9e8c66e8020676cf8f719e2e97b
FAIL predicate: no fetch always fails: got 0, expected 1
self-test: 1 failure(s) over 318 assertions
```

### E01 — Equivalent: delimiter character class to noncapturing alternation

- Point: `verifiers/check_scoped_rules.py:306`.
- Expected detector: Expected survival: `[:=]` and `(?::|=)` match the same one-character alternatives without adding captures.
- Verdict: **SURVIVED**. SURVIVED as expected; equivalent control, not a coverage finding.
- Pristine receipt: `M26.restored.json` (exit 0, before/after H). Mutated receipt: `E01.mutated.json` (exit 0). Restored receipt: `E01.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `099b3981b11a62c2a382d16216deaea01cd18639ee0f69ae44d7d8ca057c4122`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..7c28141 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -303,7 +303,7 @@ RULE_WORD_RE = re.compile(r"\b(rules?|instructions?)\b", re.IGNORECASE)
 SHA256_RE = re.compile(r"sha256[\s`*:=\[]*([0-9a-fA-F]{64})(?![0-9a-fA-F])")
 SEPARATOR_RE = re.compile(r":?-{3,}:?")
 KEY_IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
-KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*[:=]""")
+KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*(?::|=)""")
 VALUE_ONLY_RE = re.compile(r"[ \t\[\|>]*")
 VALUE_STRIP = "-[\"'` \t"
 PATTERN_TOKEN_RE = re.compile(r"^[A-Za-z0-9_./*{},!-]+$")
```

Observed stdout (stderr empty):

```text
counter sha256 099b3981b11a62c2a382d16216deaea01cd18639ee0f69ae44d7d8ca057c4122
self-test: 0 failure(s) over 318 assertions
```

### E02 — Equivalent: wildcard membership to find comparison

- Point: `verifiers/check_scoped_rules.py:830`.
- Expected detector: Expected survival: on the returned string token, `"*" in tok` iff `tok.find("*") >= 0`.
- Verdict: **SURVIVED**. SURVIVED as expected; equivalent control, not a coverage finding.
- Pristine receipt: `E01.restored.json` (exit 0, before/after H). Mutated receipt: `E02.mutated.json` (exit 0). Restored receipt: `E02.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `9687674139b761f34796d4e24227ce737188c0ae37179dd5fd6bf7cbed6682ac`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..88429ce 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -827,7 +827,7 @@ def pattern_value(text: str) -> bool:
 
     It must contain `*` and consist only of `[A-Za-z0-9_./*{},!-]`."""
     tok = first_value_token(text)
-    return "*" in tok and PATTERN_TOKEN_RE.match(tok) is not None
+    return tok.find("*") >= 0 and PATTERN_TOKEN_RE.match(tok) is not None
 
 
 def block_only(rest: str) -> bool:
```

Observed stdout (stderr empty):

```text
counter sha256 9687674139b761f34796d4e24227ce737188c0ae37179dd5fd6bf7cbed6682ac
self-test: 0 failure(s) over 318 assertions
```

### E03 — Equivalent: commute integer slice-end addition

- Point: `verifiers/check_scoped_rules.py:846`.
- Expected detector: Expected survival: integer `L + 3` equals `3 + L`; slice bounds are unchanged.
- Verdict: **SURVIVED**. SURVIVED as expected; equivalent control, not a coverage finding.
- Pristine receipt: `E02.restored.json` (exit 0, before/after H). Mutated receipt: `E03.mutated.json` (exit 0). Restored receipt: `E03.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `1cd119fe708aec74f486853b225fd0f48b0a84e6ae63a50ab7202eae6c8c1569`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..1db3eaf 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -843,7 +843,7 @@ def value_after(lines: list[str], L: int, rest: str) -> str | None:
     with `-` or a quote; any other first nonblank line leaves no value."""
     if not block_only(rest):
         return rest
-    for line in lines[L:L + 3]:
+    for line in lines[L:3 + L]:
         if not line.strip():
             continue
         return line if line.lstrip().startswith(("-", '"', "'", "`")) else None
```

Observed stdout (stderr empty):

```text
counter sha256 1cd119fe708aec74f486853b225fd0f48b0a84e6ae63a50ab7202eae6c8c1569
self-test: 0 failure(s) over 318 assertions
```

### E04 — Equivalent: integer ceiling-half identity

- Point: `verifiers/check_scoped_rules.py:891`.
- Expected detector: Expected survival: for integer cardinalities, `(n + 1) // 2` equals `-(-n // 2)`; the max floor is unchanged.
- Verdict: **SURVIVED**. SURVIVED as expected; equivalent control, not a coverage finding.
- Pristine receipt: `E03.restored.json` (exit 0, before/after H). Mutated receipt: `E04.mutated.json` (exit 0). Restored receipt: `E04.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `a14310e54608267bce995233ce264bfd57ed23ec07910366a06895fd5e3ce8b6`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..1fcfabd 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -888,7 +888,7 @@ def content_words(text: str) -> set[str]:
 
 def action_need(n_content: int) -> int:
     """The Action conjunct's threshold: max(2, ceil(|W| / 2))."""
-    return max(MIN_SHARED, (n_content + 1) // 2)
+    return max(MIN_SHARED, -(-n_content // 2))
 
 
 def action_conjunct(lines: list[str], cell: str, L: int | None) -> list[str]:
```

Observed stdout (stderr empty):

```text
counter sha256 a14310e54608267bce995233ce264bfd57ed23ec07910366a06895fd5e3ce8b6
self-test: 0 failure(s) over 318 assertions
```

### E05 — Equivalent: predicate conditional to integer boolean

- Point: `verifiers/check_scoped_rules.py:1249`.
- Expected detector: Expected survival: after the unchanged fetch/None guards and with integer counts/target, the failing comparison converts to one and the passing comparison to zero.
- Verdict: **SURVIVED**. SURVIVED as expected; equivalent control, not a coverage finding.
- Pristine receipt: `E04.restored.json` (exit 0, before/after H). Mutated receipt: `E05.mutated.json` (exit 0). Restored receipt: `E05.restored.json` (exit 0, before/after H, target diff empty).
- Variant SHA256 before = after detector: `14e7a1614348c4e3610d2d4536aa8dc8349b1c1385a5c7d702aa14c69112e1eb`.

```diff
diff --git i/verifiers/check_scoped_rules.py w/verifiers/check_scoped_rules.py
index 9d2195e..ea7d2ee 100755
--- i/verifiers/check_scoped_rules.py
+++ w/verifiers/check_scoped_rules.py
@@ -1246,7 +1246,7 @@ def predicate(fetching: bool, found: int) -> int:
     """Exit 0 iff fetching, the target is frozen and F >= TARGET."""
     if not fetching or TARGET is None:
         return 1
-    return 0 if found >= TARGET else 1
+    return int(found < TARGET)
 
 
 def _outcome(fn) -> tuple[str, object]:
```

Observed stdout (stderr empty):

```text
counter sha256 14e7a1614348c4e3610d2d4536aa8dc8349b1c1385a5c7d702aa14c69112e1eb
self-test: 0 failure(s) over 318 assertions
```

## Handoff

No counter patch is proposed and no frozen rule, target, or counter bytes are integrated. The report records eight surviving behavioral variants with their conditional production-path relevance, plus five expected equivalent survivors. All scratch counter bytes are restored to H; each restoration reran the assigned detector successfully. Only the L1 decides any subsequent action under the frozen measurement protocol.

Report: .ufo/waves/round-60/build/MutC1Counter.md
