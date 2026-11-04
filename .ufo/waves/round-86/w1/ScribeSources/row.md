# ScribeSources — registry row (round 86)

- Next free id computed: `grep -oE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md | sort | tail -1` → `| S254`, so the new id is **S255**.
- Row appended at `corpus/SOURCES.md` line 196 (directly after S254, last row of `## Registry`); 11 cells (`awk -F'|' 'NR==196{print NF-2}'` → `11`); no literal `|` inside a cell; LF only (`grep -c $'\r'` → `0`); `git diff --numstat` → `1 0 corpus/SOURCES.md` (one line added, nothing else changed).
- Cells: S255 | omp 18.15.0 embedded TypeScript (ELF path, sha256 6737ee24…, upstream https://github.com/can1357/oh-my-pi tag v18.15.0, HTTP 200) | code | A | scope as assigned | ELF module offsets | teaches | mined | 2026-11-04 | on-release | corpus/knowledge/omp-catalogue-model-round86.md, verifiers/omp-skill-roots.tsv
- Receipt: `.ufo/waves/round-86/w1/ScribeSources/fetch-record.txt`.
