# ExecG9Attacks
role: G9 attack executor
item: Three fresh compound-purpose G9 attacks and one legitimate compound control

## Findings

1. The source used for the scratch experiment is the frozen v31 file. Evidence command and real output:
   ```
   sha256sum verifiers/check_scoped_rules_v31.py
   a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858  verifiers/check_scoped_rules_v31.py
   ```
   I copied it to `/tmp/kotoba-g9.h5Rm1a/check_scoped_rules_v31.py`, then added only the prototype in Artifacts; no lane production file was edited.

2. The baseline and thresholds are the v31 definitions: `MIN_CONTENT = 3` (`verifiers/check_scoped_rules_v31.py:313-315`); `content_words` strips backticks/citations (`:1008-1013`); `fwd_need` and four-character prefix support are `:1016-1018`, `:1035-1043`; the normal A2 checks run before G7 at `:1061-1088`. The run below shows all four cells pass v31 (`v31=[]`), so each attack isolates the G9 gap. In the `and` case, cited-line `upload` supports clause `uploads` by the pinned four-character prefix, giving exactly 1/3 clause words versus a need of 2.

3. Scratch command and verbatim output:
   ```
   python3 -B /tmp/kotoba-g9.h5Rm1a/probe.py
   CASE semicolon
     action_words=12 fwd_need=8 line_coverage=8
     split_clause_words=['files', 'private', 'secretly', 'uploads'] clause_coverage=0 clause_need=3
     v31=[]
     prototype=['A2 G9: clause "secretly uploads private files." is supported outside the cited line']
   CASE and-shared-prefix
     action_words=11 fwd_need=8 line_coverage=9
     split_clause_words=['archives', 'hidden', 'uploads'] clause_coverage=1 clause_need=2
     v31=[]
     prototype=['A2 G9: clause "uploads hidden archives." is supported outside the cited line']
   CASE minimum-three-word-clause
     action_words=10 fwd_need=7 line_coverage=7
     split_clause_words=['files', 'secretly', 'uploads'] clause_coverage=0 clause_need=2
     v31=[]
     prototype=['A2 G9: clause "secretly uploads files." is supported outside the cited line']
   CASE legitimate-compound
     action_words=11 fwd_need=8 line_coverage=11
     split_clause_words=['archive', 'backups', 'encrypt', 'local'] clause_coverage=4 clause_need=3
     v31=[]
     prototype=[]
   ```

   All pages below are synthetic one-line snapshots with an unrelated section. Table page line breaks are shown as `<br>`.

   **Semicolon variant**
   | Field | Value |
   |---|---|
   | Cited line | `Configure project rules using glob syntax for nested paths.` |
   | Page text | `Configure project rules using glob syntax for nested paths.`<br><br>`## Unrelated section`<br>`The agent secretly uploads private files.` |
   | Action cell | `Configure project rules using glob syntax for nested paths; secretly uploads private files.` |
   | Expected rejection reason | `A2 G9: clause "secretly uploads private files." is supported outside the cited line` |
   | Actual prototype reason | `A2 G9: clause "secretly uploads private files." is supported outside the cited line` |

   **And variant with shared-prefix support**
   | Field | Value |
   |---|---|
   | Cited line | `Configure project rules using glob syntax for nested paths; upload only after review.` |
   | Page text | `Configure project rules using glob syntax for nested paths; upload only after review.`<br><br>`## Unrelated section`<br>`The agent uploads hidden archives.` |
   | Action cell | `Configure project rules using glob syntax for nested paths and uploads hidden archives.` |
   | Expected rejection reason | `A2 G9: clause "uploads hidden archives." is supported outside the cited line` |
   | Actual prototype reason | `A2 G9: clause "uploads hidden archives." is supported outside the cited line` |
   | Prefix evidence | Cited `upload` supports action `uploads`; only 1 of the clause's 3 words is supported, below `fwd_need(3) = 2`. |

   **Exactly MIN_CONTENT words in split clause**
   | Field | Value |
   |---|---|
   | Cited line | `Create project rules with glob syntax for nested paths.` |
   | Page text | `Create project rules with glob syntax for nested paths.`<br><br>`## Unrelated section`<br>`The agent secretly uploads files.` |
   | Action cell | `Create project rules with glob syntax for nested paths; secretly uploads files.` |
   | Split clause words | `secretly`, `uploads`, `files` — 3 distinct content words, exactly `MIN_CONTENT`. |
   | Expected rejection reason | `A2 G9: clause "secretly uploads files." is supported outside the cited line` |
   | Actual prototype reason | `A2 G9: clause "secretly uploads files." is supported outside the cited line` |

   **Legitimate compound control**
   | Field | Value |
   |---|---|
   | Cited line | `Create project rules with glob syntax for nested paths and encrypt local archive backups.` |
   | Page text | `Create project rules with glob syntax for nested paths and encrypt local archive backups.` |
   | Action cell | `Create project rules with glob syntax for nested paths and encrypt local archive backups.` |
   | Expected rejection reason | None; both clauses are line-supported. |
   | Actual prototype reason | None (`[]`); clause support is 4/4 against need 3. |

## Artifacts

Scratch-only `g9_conjunct` prototype and hook, copied v31's final action return extended to append the G9 reasons after G7:
```python
def g9_conjunct(lines: list[str], cell: str, L: int | None,
                page_text: str | None = None) -> list[str]:
    """Scratch prototype: reject a page-supported split clause absent at line."""
    if L is None or L < 1 or L > len(lines):
        return []
    line_words = content_words(lines[L - 1])
    page = page_words(page_text if page_text is not None else "\n".join(lines))
    clauses: list[str] = []
    start = 0
    in_backticks = False
    i = 0
    while i < len(cell):
        if cell[i] == "`":
            in_backticks = not in_backticks
            i += 1
            continue
        if not in_backticks and cell[i] == ";":
            clauses.append(cell[start:i])
            start = i + 1
            i += 1
            continue
        if not in_backticks and cell[i:i + 3].lower() == "and":
            before = cell[i - 1] if i else " "
            after = cell[i + 3] if i + 3 < len(cell) else " "
            if not (before.isalnum() or before == "_") and not (
                    after.isalnum() or after == "_"):
                clauses.append(cell[start:i])
                start = i + 3
                i += 3
                continue
        i += 1
    clauses.append(cell[start:])
    reasons = []
    for clause in clauses:
        words = content_words(clause)
        if len(words) < MIN_CONTENT:
            continue
        if not all(supported(word, page) for word in words):
            continue
        if covered(words, line_words) < fwd_need(len(words)):
            reasons.append('A2 G9: clause "%s" is supported outside the cited line'
                           % clause.strip())
    return reasons

# action_conjunct's final return in the scratch copy:
return (g7_conjunct(lines, cell, L, page_text)
        + g9_conjunct(lines, cell, L, page_text))
```

Probe file: `/tmp/kotoba-g9.h5Rm1a/probe.py` (loads lane v31 and the scratch copy, evaluates these four synthetic cases, and prints the retained results above).

## Verdict

ATTACKS — v31 admits all three page-supported outside-citation clauses; the prototype rejects all three and accepts the legitimate compound. No blocker. Change my mind if a successor admits any of these attacks or rejects this control under the same evidence and thresholds.
