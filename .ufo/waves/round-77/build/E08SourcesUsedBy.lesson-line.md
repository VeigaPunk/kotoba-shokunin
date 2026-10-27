# E08SourcesUsedBy — the exact old -> new line for `corpus/lessons/round-76.md` § Status changes
#
# House format: corpus/lessons/round-66.md, § "SOURCES used-by correction (append-only)".
# C1 conjunct (e) accepts this line: measured at a scratch commit whose only lesson content is the
# "## Status changes" section below — `(e) registry: pass`, exit 1 overall (other conjuncts fail
# because a stub entry has no quotes/audit), receipt desccraft-E-logline.txt.
# Paste as one bullet under the lesson's "## Status changes" heading (no blank line inside the bullet).

## Status changes

- S213 `used-by` old -> new: `corpus/knowledge/skill-eval-artefacts-round70.md` -> `corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md`. The entry `corpus/knowledge/description-craft-round76.md` is the new consumer (C1); the separator is comma + space, the one the census splits on (`scripts/sources-census.sh`, `usedby_findings`). `status` remains `mined`; `recheck` remains `90d`; `opened` remains 2026-10-25; every other cell is unchanged, including the `anchor` cell (CORPUS.md rule 2 forbids in-place changes there). Append-only gate at this change: `log … S213 used-by: …round70.md -> …round70.md, corpus/k…`, 18 pre-existing breaches in 8 of 45 commits, 0 new.
