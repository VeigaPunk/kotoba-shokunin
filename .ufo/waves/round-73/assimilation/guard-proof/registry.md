# Guard proof — scratch registry (not a lane file, not a registry the lane lands)

One column-zero row and one **one-space-indented** row, both registry-shaped. The maintained
parser (`sources-census.sh`) documents that it accepts 0–3 leading ASCII spaces before Markdown
rows; the frozen manual extraction pattern carries the same bound. This file is the fixture that
shows the two differ on indentation.

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Zero-indent scratch row — https://guard-proof.example/zero | docs | B | column-zero control | § 1 | the column-zero control row | mined | 2026-10-24 | 90d | — |
 | S234 | Indented scratch row — https://guard-proof.example/indented | docs | B | one-space-indent | § 2 | the indented row the guard must still find | mined | 2026-10-24 | 90d | — |
