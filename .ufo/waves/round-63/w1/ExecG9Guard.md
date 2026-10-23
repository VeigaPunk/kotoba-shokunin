# ExecG9Guard
role: G9 guard executor (depth)
item: Deliver the G9 clause splitter, guard function, and `action_conjunct` append line for the new v32 counter.

## Findings
1. `plans/round-63.md:51-58` defines the guard: split at `;` and case-insensitive `and` outside backticks, apply the A2 forward threshold to clauses with at least `MIN_CONTENT` words, and limit this guard to page-present clauses. It also requires appending G9 reasons after G7 reasons.
2. `verifiers/check_scoped_rules_v31.py:314-315` sets `MIN_CONTENT = 3`; `:352-354` sets `FWD_NUM, FWD_DEN = 2, 3` and `SUPPORT_PREFIX = 4`.
3. `verifiers/check_scoped_rules_v31.py:1008-1043` provides `content_words`, `fwd_need`, `page_words`, `supported`, and `covered`; the proposed function reuses these unchanged.
4. `verifiers/check_scoped_rules_v31.py:1046-1088` shows G7's signature and the current successful-path return `return g7_conjunct(lines, cell, L, page_text)`, which the proposed one-line change extends.
5. Splitter limits: `R and D`-style abbreviations are treated as coordination (and short pieces can fall below `MIN_CONTENT`); ordinary single/double-quoted `and` is not protected (only backticks are); hyphenated compounds such as `rock-and-roll` split at `and`. Escaped or unmatched backticks and nested/backtick-run markdown are not parsed specially; the helper toggles state on each literal backtick.

## Artifacts

Module-level splitter regex constant and helper:
```python
ACTION_AND_RE = re.compile(r"\band\b", re.IGNORECASE)


def split_action_clauses(cell: str) -> list[str]:
    """Split at semicolons and the word 'and', except inside backticks."""
    clauses = []
    start = 0
    in_backticks = False
    i = 0
    while i < len(cell):
        if cell[i] == "`":
            in_backticks = not in_backticks
            i += 1
            continue
        if not in_backticks:
            if cell[i] == ";":
                clauses.append(cell[start:i])
                start = i + 1
                i += 1
                continue
            match = ACTION_AND_RE.match(cell, i)
            if match is not None:
                clauses.append(cell[start:i])
                start = match.end()
                i = match.end()
                continue
        i += 1
    clauses.append(cell[start:])
    return clauses
```

Full proposed G9 function:
```python
def g9_conjunct(lines: list[str], cell: str, L: int | None,
                page_text: str | None = None) -> list[str]:
    """Require page-present action clauses to meet A2 forward support at L."""
    if L is None or L < 1 or L > len(lines):
        return []
    line_w = content_words(lines[L - 1])
    page = page_words(page_text if page_text is not None else "\n".join(lines))
    reasons = []
    for clause in split_action_clauses(cell):
        words = content_words(clause)
        if len(words) < MIN_CONTENT:
            continue
        if any(not supported(word, page) for word in words):
            continue
        if covered(words, line_w) < fwd_need(len(words)):
            reasons.append(
                'A2 G9: clause "%s" is supported outside the cited line'
                % clause.strip())
    return reasons
```

Exact replacement line in `action_conjunct`:
```python
return g7_conjunct(lines, cell, L, page_text) + g9_conjunct(lines, cell, L, page_text)
```

## Verdict
PROPOSES — this design follows the frozen predicate and reuses v31 scoring helpers without changing their semantics. I would revise it if a frozen fixture demonstrates a different definition of page-present support or delimiter handling. No lane production files were changed; this report is the only artifact written.