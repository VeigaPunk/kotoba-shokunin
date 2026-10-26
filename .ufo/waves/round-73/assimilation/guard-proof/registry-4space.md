# Guard proof — boundary fixture: a row indented by FOUR spaces

Four or more spaces are an indented code block, not a table row, for both the maintained parser
and the frozen extraction pattern. The boundary is therefore the same on both sides.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Zero-indent scratch row — https://guard-proof.example/zero | docs | B | column-zero control | § 1 | the column-zero control row | mined | 2026-10-24 | 90d | — |
    | S235 | Four-space row — https://guard-proof.example/four-space | docs | B | four-space | § 3 | a row the parser must treat as code | mined | 2026-10-24 | 90d | — |
