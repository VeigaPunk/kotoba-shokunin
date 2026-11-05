# Round 87 evidence index (w3, seat ScribeIndexR87)

Snapshot: 2026-11-05T00:17:52-03:00. Lane `master` = `d1c031833c37af99196f72f84a6643f84eec129a`. Every row below was produced by a stat, a read, or a `git cat-file` at the snapshot; the tree is live (peer seats still write under `w3/`), so counts are for this snapshot only.

Legend: `T` tracked at lane master, `U` untracked or modified. "Revisions/hashes named" lists the first hex tokens (7–40 chars) in the file; "commands recorded" lists the first lines that look like a command.

## 1. Round-87 tree: 129 files

| path | bytes | trk | first line | revisions/hashes named | commands recorded |
|---|---:|:-:|---|---|---|
| `.ufo/waves/round-87/INHERITED-w2.txt` | 1061 | T | # Inherited: a second L1 (`KotobaR87a3`) built a round-87 wave-2 spec at 21:02:32-44 on th | fcdaba57 | none recorded |
| `.ufo/waves/round-87/build-after-battery.sh` | 1326 | T | #!/bin/sh | — | run corpus_integrity python3 -B verifiers/verify_corpus_integrity.py ; run corpus_independent python3 -B verifiers/verify_corpus_independent.py |
| `.ufo/waves/round-87/build-base-battery.sh` | 1234 | T | #!/bin/sh | 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | run corpus_integrity python3 -B verifiers/verify_corpus_integrity.py ; run corpus_independent python3 -B verifiers/verify_corpus_independent.py --json |
| `.ufo/waves/round-87/gen-w1.py` | 37665 | T | #!/usr/bin/env python3 | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 669f2801c31ef27e18cc35a327d2e18f466281c7, 04647b0f715ff3c4f314b0d8f03dea28bc453688 | C1 (depth): `python3 -B verifiers/check_omp_root_semantics.py --rev <rev>` prints ; `omp root semantics grounded N of 13`, exit 0 iff N == 13 and guards S1-S3 PASS. New ledge |
| `.ufo/waves/round-87/gen-w3.py` | 25047 | T | #!/usr/bin/env python3 | 669f2801, 512126bb, 87ab1cb9, 760e1c5edfdefb4767420f711d08f669952de013 | find, naming it). Installed omp ELF: /home/vgpnk/.local/bin/omp, sha256 {ELF}. ; - C1 depth: `python3 -B verifiers/check_omp_root_semantics.py --rev <rev>` -> `omp root se |
| `.ufo/waves/round-87/r87-w1-dispatch.err` | 0 | T |  | — | none recorded |
| `.ufo/waves/round-87/r87-w1-dispatch.json` | 131784 | T | { | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 669f2801c31ef27e18cc35a327d2e18f466281c7, 04647b0f715ff3c4f314b0d8f03dea28bc453688 | "milestone": "r87-w1: C1 depth — omp root semantics grounded per root (13 rows: code reade ; "milestone": "r87-w1: C1 depth — omp root semantics grounded per root (13 rows: code reade |
| `.ufo/waves/round-87/r87-w1-results.json` | 10281 | T | { | dca21dee, 65590472, 6737ee24, 223ae62 | "output": "{\n  \"seat\": \"ReviewerC1\",\n  \"files_written\": [\n    \".ufo/waves/round- |
| `.ufo/waves/round-87/r87-w1-spec.json` | 120099 | T | { | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 669f2801c31ef27e18cc35a327d2e18f466281c7, 04647b0f715ff3c4f314b0d8f03dea28bc453688 | "milestone": "r87-w1: C1 depth — omp root semantics grounded per root (13 rows: code reade ; "context": "## Bounds (read first)\nLane repo: /home/vgpnk/Projects/shokunin/kotoba-shokun |
| `.ufo/waves/round-87/r87-w1.ready` | 162 | T | {"lane":"kotoba","round":87,"wave":"r87-w1","dispatch":"/home/vgpnk/Projects/shokunin/koto | — | none recorded |
| `.ufo/waves/round-87/r87-w1.ready.dispatched` | 435 | T | 2026-11-04T20:11:31 | — | none recorded |
| `.ufo/waves/round-87/r87-w3-dispatch.err` | 0 | T |  | — | none recorded |
| `.ufo/waves/round-87/r87-w3-dispatch.json` | 89841 | T | { | 669f2801c31ef27e18cc35a327d2e18f466281c7, 512126bbd762ff82b9f330c4afefb29db7cd9f39, 87ab1cb98b4950f5d7291a4a2ddaab535ca72124, 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | "context": "## Bounds (read first)\nLane repo: /home/vgpnk/Projects/shokunin/kotoba-shokun ; "task": "/skill:godspeed\n\n## Bounds (read first)\nLane repo: /home/vgpnk/Projects/shokun |
| `.ufo/waves/round-87/r87-w3-spec.json` | 80689 | T | { | 669f2801c31ef27e18cc35a327d2e18f466281c7, 512126bbd762ff82b9f330c4afefb29db7cd9f39, 87ab1cb98b4950f5d7291a4a2ddaab535ca72124, 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | "context": "## Bounds (read first)\nLane repo: /home/vgpnk/Projects/shokunin/kotoba-shokun ; "prompt": "## Bounds (read first)\nLane repo: /home/vgpnk/Projects/shokunin/kotoba-shokuni |
| `.ufo/waves/round-87/r87-w3.ready` | 162 | T | {"lane":"kotoba","round":87,"wave":"r87-w3","dispatch":"/home/vgpnk/Projects/shokunin/koto | — | none recorded |
| `.ufo/waves/round-87/r87-w3.ready.dispatched` | 467 | T | 2026-11-05T00:08:39 | — | none recorded |
| `.ufo/waves/round-87/receipts/after-battery.txt` | 17893 | T | tip ff4bf3fd70662f20ab066eee6fde4bd605aa07b6 | ff4bf3fd70662f20ab066eee6fde4bd605aa07b6, 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1, 7bb48f213ac677f943d5c791199ed3dddf302f00, 25cc5c7b | verifiers/fault_injection_corpus.sh          OK ; rev ff4bf3fd70662f20ab066eee6fde4bd605aa07b6 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 |
| `.ufo/waves/round-87/receipts/base-battery.txt` | 18635 | T | base 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1, 7bb48f213ac677f943d5c791199ed3dddf302f00, 25cc5c7b | verifiers/fault_injection_corpus.sh          OK |
| `.ufo/waves/round-87/receipts/c1-after-tip.txt` | 1677 | T | rev ff4bf3fd70662f20ab066eee6fde4bd605aa07b6 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 | ff4bf3fd70662f20ab066eee6fde4bd605aa07b6, 173819979, 173840364, 173865724 | rev ff4bf3fd70662f20ab066eee6fde4bd605aa07b6 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show ff4bf3fd70662f20ab066eee6fde4bd605aa07b6:verifiers |
| `.ufo/waves/round-87/receipts/c1-after.txt` | 1677 | T | rev e03f9e226b51b8cb94f2dc5c7c3027c5286b004b elf /home/vgpnk/.local/bin/omp sha256 6737ee2 | e03f9e226b51b8cb94f2dc5c7c3027c5286b004b, 173819979, 173840364, 173865724 | rev e03f9e226b51b8cb94f2dc5c7c3027c5286b004b elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show e03f9e226b51b8cb94f2dc5c7c3027c5286b004b:verifiers |
| `.ufo/waves/round-87/receipts/c1-instrument-freeze.txt` | 400 | T | counter: verifiers/check_omp_root_semantics.py sha256 6e826f3bf8d4585340ddcc9b7a546e4b7d8b | 223ae62 | omp root semantics grounded 0 of 12 |
| `.ufo/waves/round-87/receipts/c2-after.txt` | 578 | T | PASS d1  two receipts carry exit=0; instruments equal 04647b0f..ff4bf3fd | 04647b0f, ff4bf3fd, 223ae624 | none recorded |
| `.ufo/waves/round-87/receipts/c2-final.txt` | 578 | T | PASS d1  two receipts carry exit=0; instruments equal 04647b0f..35a395a9 | 04647b0f, 35a395a9, 223ae624 | none recorded |
| `.ufo/waves/round-87/receipts/census-after.txt` | 3078 | T | kotoba?W04?S018 duplicate url agentskills.io/specification across scopes | — | none recorded |
| `.ufo/waves/round-87/receipts/d5-after-revert.txt` | 1206 | T | D5 after the revert of the two laundered records (round 87, L1 integration, 2026-11-04) | ae3f49a3685e796ae5154cf9a4b055132a8c25b0, 315c0ec68075e9c7c4037b8f42617e3eee0a434b, ae3f49a, 315c0ec | $ git checkout -- corpus/lessons/round-86-verifier-spotcheck.md corpus/lessons/round-81.md ; $ git rev-parse :corpus/lessons/round-86-verifier-spotcheck.md :corpus/lessons/round-81.md |
| `.ufo/waves/round-87/receipts/province-core-tip.txt` | 119 | T | measured-rev: fcdaba57fe00c92237e6b865fea860eb93a9fc6d | fcdaba57fe00c92237e6b865fea860eb93a9fc6d | none recorded |
| `.ufo/waves/round-87/w1/ExecLedger/build_ledger.py` | 2282 | T | import subprocess, sys, mmap, json | 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | none recorded |
| `.ufo/waves/round-87/w1/ExecLedger/receipts-elf-reads.txt` | 12078 | T | ExecLedger ? round-87 w1 ? verifiers/omp-skill-roots-semantics.tsv receipt | 276785328, 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 173819979, 173814223 | instrument: python3 stdlib only, mmap+re over the installed ELF; the ELF was never copied. ; $ sha256sum /home/vgpnk/.local/bin/omp |
| `.ufo/waves/round-87/w1/ExecLedger/recheck.py` | 2561 | T | import mmap, subprocess, hashlib, sys | 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | none recorded |
| `.ufo/waves/round-87/w1/ExecLedger/verify.py` | 3479 | T | import mmap, re, sys, json | — | none recorded |
| `.ufo/waves/round-87/w1/ExecRepairs/base.txt` | 1774 | T | # C2 counter ? base reading, freeze reading, self-test | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 223ae62424f8, 669f2801c31ef27e18cc35a327d2e18f466281c7, 669f2801c31e | $ sha256sum verifiers/check_r86_routed_repairs.py ; $ python3 -B verifiers/check_r86_routed_repairs.py --self-test |
| `.ufo/waves/round-87/w1/ExecRepairs/d5-clone-diagnostic.txt` | 2372 | T | # D5 shape diagnostic ? why the clone reading differs from the lane reading | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 223ae62, 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1 | $ python3 -B verifiers/verify_corpus_integrity.py > out.txt   # cwd=$S/repo-probe (clone o ; $ python3 -B verifiers/verify_corpus_integrity.py --json   # drift sites |
| `.ufo/waves/round-87/w1/ExecRepairs/worlds.txt` | 3552 | T | # C2 worlds, scored on the frozen counter (fixture worlds from --self-test shapes) | 60f7448648ac0c7a40e769435abfe9b0553a3809, 85134a78ddf694a36bf66963b35db1e3d83ec68a, 60f74486, 85134a78 | $ python3 -B $S/worlds_probe.py |
| `.ufo/waves/round-87/w1/ExecSemantics/base.txt` | 809 | T | rev 223ae62424f8ab1eb365d733eb648d6228ddd7e8 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 | 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | rev 223ae62424f8ab1eb365d733eb648d6228ddd7e8 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show 223ae62424f8ab1eb365d733eb648d6228ddd7e8:verifiers |
| `.ufo/waves/round-87/w1/ExecSemantics/freeze.txt` | 809 | T | rev 669f2801c31ef27e18cc35a327d2e18f466281c7 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 | 669f2801c31ef27e18cc35a327d2e18f466281c7 | rev 669f2801c31ef27e18cc35a327d2e18f466281c7 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show 669f2801c31ef27e18cc35a327d2e18f466281c7:verifiers |
| `.ufo/waves/round-87/w1/ExecSemantics/reference-ledger-probe.txt` | 1793 | T | rev 3ce6173cdf7b940e2247909634bb9e0c3d413c79 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 | 3ce6173cdf7b940e2247909634bb9e0c3d413c79, 173819979, 173840364, 173865523 | rev 3ce6173cdf7b940e2247909634bb9e0c3d413c79 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show 3ce6173cdf7b940e2247909634bb9e0c3d413c79:verifiers |
| `.ufo/waves/round-87/w1/ExecSemantics/selftest.txt` | 39 | T | 0 failure(s) over 35 assertions | — | none recorded |
| `.ufo/waves/round-87/w1/MutTester/mutate_run.py` | 4576 | T | #!/usr/bin/env python3 | — | 1. python3 -B <copy> --self-test ; 2. python3 -B <copy> <honest argv...> |
| `.ufo/waves/round-87/w1/ReviewerC1.md` | 9684 | T | # ReviewerC1 ? attack C1's four conjuncts (round 87, w1) | dca21dee7432defc, 99a11d5c, 65590472569fc3b9, b77475cb | - omp ELF sha256 `6737ee2415555a36…49ccb7b0f` (matches the plan pin; S2 PASS everywhere) ; Mine: `omp root semantics grounded 12 of 12`, guards S1/S2/S3 PASS, exit 0. |
| `.ufo/waves/round-87/w1/ReviewerC1/driver_worlds.py` | 7627 | T | #!/usr/bin/env python3 | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 173814223, 173814308, 114486488 | python3 -B driver_worlds.py --real-ledger <path-to-real-semantics.tsv> \ ; W_DOC_LINE = 'var Js = "Native OMP configuration from ~/.omp and .omp/";' |
| `.ufo/waves/round-87/w1/ReviewerC1/indep_root_semantics.py` | 12953 | T | #!/usr/bin/env python3 | 512126b | 2 reader   reader_quote (>= 12 chars) occurs verbatim in the omp ELF AND on an ELF line ; Independent of ExecSemantics' counter (own code, own ELF scan). Stdlib only, python3 -B, |
| `.ufo/waves/round-87/w1/ReviewerC1/probe_bound.py` | 2791 | T | #!/usr/bin/env python3 | — | Usage: python3 -B probe_bound.py --counter <path to check_omp_root_semantics.py> |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/base223-observed.txt` | 802 | T | rev 223ae62424f8ab1eb365d733eb648d6228ddd7e8 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 | 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | rev 223ae62424f8ab1eb365d733eb648d6228ddd7e8 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show 223ae62424f8ab1eb365d733eb648d6228ddd7e8:verifiers |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/probe-bound.out` | 4239 | T | counter source: 29974 bytes | — | CALL syn_roots('/home/u/proj/sub',) -> 'root_pattern\tbinary_quote\n/\tNative OMP configur ; CALL syn_roots('{cwd}/.omp/skills',) -> 'root_pattern\tbinary_quote\n{\tNative OMP configu |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/real-score-indep.txt` | 2652 | T | S1 ledger-from-rev: semantics rc=0 (1939 B), roots rc=0 (986 B) [git show bytes, never wor | — | S1 ledger-from-rev: semantics rc=0 (1939 B), roots rc=0 (986 B) [git show bytes, never wor ; omp root semantics grounded 12 of 12 |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/recon_elf.out` | 312560 | T | ELF bytes 276785328 | 276785328, 170198491, 170105142, 170324629 | none recorded |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/recon_readers.out` | 1521 | T | min header offset: 166865730 (doc string-table first occurrence @114486488) | 166865730, 114486488, 173814223, 173832353 | none recorded |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/recon_readers2.out` | 1278 | T | == ALL join lines in agents.ts body [173864077, 173869755): | 173864077, 173869755, 173865521, 173865716 | none recorded |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/recon_worlds2.out` | 2196 | T | header occurrence lists: | 173809529, 173814223, 173869756, 173878972 | count=  2 first@ 114486488  'Native OMP configuration from ~/.omp and .omp/' ; @173814308 len=58 occ=1 'var Js = "Native OMP configuration from ~/.omp and .omp/";' |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/reference-ledger.tsv` | 1994 | T | root_pattern?binary_quote?module?reader_quote | — | {cwd}/.omp/skills	Native OMP configuration from ~/.omp and .omp/	coding-agent/src/discover ; ~/.omp/agent/skills	Native OMP configuration from ~/.omp and .omp/	coding-agent/src/discov |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/reference-score.txt` | 2653 | T | S1 ledger-from-rev: semantics rc=0 (1994 B), roots rc=0 (986 B) [git show bytes, never wor | — | S1 ledger-from-rev: semantics rc=0 (1994 B), roots rc=0 (986 B) [git show bytes, never wor ; omp root semantics grounded 12 of 12 |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/worlds-indep-real.txt` | 941 | T | real-baseline \| omp root semantics grounded 12 of 12 \| exit=0 | — | real-baseline \| omp root semantics grounded 12 of 12 \| exit=0 ; W1a-docjoin-line \| omp root semantics grounded 11 of 12 \| exit=1 \| row  1 red    c1=True   |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/worlds-indep.txt` | 660 | T | world_real \| omp root semantics grounded 12 of 12 \| exit=0 \| my-scorer baseline | — | world_real \| omp root semantics grounded 12 of 12 \| exit=0 \| my-scorer baseline ; W1a-docjoin-line \| omp root semantics grounded 11 of 12 \| exit=1 \| row1 red c1=True c2=Fal |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/worlds-summary.txt` | 504 | T | world_real \| omp root semantics grounded 12 of 13 \| exit=1 | — | world_real \| omp root semantics grounded 12 of 13 \| exit=1 ; W1a-docjoin-line \| omp root semantics grounded 11 of 13 \| exit=1 |
| `.ufo/waves/round-87/w1/ReviewerC1/receipts/worlds.txt` | 6676 | T | # ReviewerC1 world receipts (counter sha256 dca21dee7432defc?) | dca21dee7432defc, 8476792ee80ca6b29971d9699b3d46264de2ae17, 173914936, 173865523 | omp root semantics grounded 12 of 13 ; omp root semantics grounded 11 of 13 |
| `.ufo/waves/round-87/w1/ReviewerC1/recon_elf.py` | 3547 | T | #!/usr/bin/env python3 | — | b"Native OMP configuration from ~/.omp and .omp/", |
| `.ufo/waves/round-87/w1/ReviewerC1/recon_readers.py` | 2537 | T | #!/usr/bin/env python3 | 114486488 | none recorded |
| `.ufo/waves/round-87/w1/ReviewerC1/recon_readers2.py` | 2158 | T | #!/usr/bin/env python3 | 173864077, 173869755, 173898271, 173906255 | none recorded |
| `.ufo/waves/round-87/w1/ReviewerC1/recon_worlds2.py` | 2871 | T | #!/usr/bin/env python3 | 173814223 | b'Native OMP configuration from ~/.omp and .omp/']: |
| `.ufo/waves/round-87/w1/ReviewerC1/worlds_indep.py` | 3014 | T | #!/usr/bin/env python3 | — | W_DOC_LINE = 'var Js = "Native OMP configuration from ~/.omp and .omp/";' ; W_DOC_BARE = "Native OMP configuration from ~/.omp and .omp/" |
| `.ufo/waves/round-87/w1/ScoutPlugin.md` | 8836 | T | # ScoutPlugin ? the plugin registry branch and C1's new source row (round 87, w1) | 166892325, 166892424, 166884479, 166892466 | Host: Linux `7.2.11-arch1-1`, omp 18.15.0, ELF `/home/vgpnk/.local/bin/omp` ; ### What omp reads under `~/.omp/plugins/` |
| `.ufo/waves/round-87/w1/ScoutPlugin/SOURCE_RECORD.txt` | 3417 | T | # ScoutPlugin SOURCE_RECORD.txt -- the fetch record for C1's new corpus/SOURCES.md row | 173914407, 173914936, 114492956, 173922491 | # claim: C1 (depth) "Sourced" conjunct -- one row opened THIS round on the omp skill-loade ; $ python3 -B  # mmap the ELF, m.find(b'dir: Zo.join(R.path, "skills"),') -> 173914936 |
| `.ufo/waves/round-87/w1/ScoutPlugin/registry.txt` | 25154 | T | # ScoutPlugin registry.txt -- the plugin registry branch on this host (round 87, 2026-11-0 | 166865730, 173713770, 173914407, 173713555 | # Host: Linux 7.2.11-arch1-1, omp 18.15.0 (/home/vgpnk/.local/bin/omp sha256 6737ee2415555 ; $ find /home/vgpnk/.omp/plugins -maxdepth 4 -printf '%y %10s %p\n' \| sort -k3   # does NOT |
| `.ufo/waves/round-87/w1/ScoutPlugin/skill-size.txt` | 978 | T | # ScoutPlugin skill-size.txt -- SKILL.md size measures for the L1 considerthese item (roun | 223ae62, 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | $ wc -l SKILL.md ; $ wc -c SKILL.md |
| `.ufo/waves/round-87/w1/ScribeLesson/census-before.txt` | 3078 | T | kotoba?W04?S018 duplicate url agentskills.io/specification across scopes | — | none recorded |
| `.ufo/waves/round-87/w1/ScribeLesson/mistake-corpus-integrity.txt` | 3625 | T | # corpus-integrity failing-set drift (round 87, seat ScribeLesson, 2026-11-04T23:31:19Z) | 669f280, 223ae62, 99c217423bc0feff33ca46a99ddc98bd6bda09c1, 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | $ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B verifiers/verify_corpus_i ; $ sed -n '31,32p' .ufo/waves/round-86/receipts/tip-remeasure.txt |
| `.ufo/waves/round-87/w1/ScribeLesson/skill-size.txt` | 952 | T | # SKILL.md size measurement (round 87, seat ScribeLesson, 2026-11-04T23:26:42Z) | 9b040edb6c3fb129596e12d4e634bb2fb04ab067, 314e4a1 | # $ git rev-parse HEAD ; # $ git show 314e4a1:SKILL.md \| wc -lc   (considerthese/2026-10-26.md basis rev) |
| `.ufo/waves/round-87/w1/swarm-registry.json` | 5183 | T | { | — | "milestone": "r87-w1: C1 depth — omp root semantics grounded per root (13 rows: code reade ; "milestone": "r87-w1: C1 depth — omp root semantics grounded per root (13 rows: code reade |
| `.ufo/waves/round-87/w3/ConnectOverlapR87.md` | 5413 | U | # ConnectOverlapR87 ? staged-package and sibling-lane overlap (read-only) | e03f9e2, 45c35e40, 3fedf8d5, 6737ee24 | - `knowledge/` holds 88 entries; none named for omp loader semantics. ; source entirely*: the omp ELF / `discovery/omp-plugins.ts` reader. Same id, |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/attribution.txt` | 4966 | U | headers in ELF: 3131; first=(166865730, 'utils/src/dirs.ts'); last=(194305276, 'mnemopi/sr | 166865730, 194305276, 173819979, 173814223 | none recorded |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/c1-tip.txt` | 3769 | U | # C1 counter at the two tips (brief's named tip, then the tip that master actually carries | d1c031833c37af99196f72f84a6643f84eec129a, 760e1c5edfdefb4767420f711d08f669952de013, 173819979, 173840364 | $ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse master ; rev 760e1c5edfdefb4767420f711d08f669952de013 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/c2-tip.txt` | 503 | U | PASS d1  two receipts carry exit=0; instruments equal 04647b0f..d1c03183 | 04647b0f, d1c03183 | none recorded |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/elf-bytes.txt` | 4841 | U | # ELF byte evidence (installed omp; sha256 6737ee24?); offsets are byte offsets from grep  | 6737ee24, 173914936, 172785704, 173879095 | $ sha256sum /home/vgpnk/.local/bin/omp |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/forgery-ledger-diffs.txt` | 2012 | U | === cb93b3a88e1fe0dd35931d40adc66c8f1f4881c9 : semantics-ledger diff vs d1c0318 (only the  | cb93b3a88e1fe0dd35931d40adc66c8f1f4881c9, d1c0318, 0ff420103b3b312cf105cc8608bc00545049a555, 27f93ebbe34f1d4875799660c571e23aa5554200 | none recorded |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/forgery-worlds.txt` | 3760 | U | fixture base: d1c031833c37af99196f72f84a6643f84eec129a  toplevel=/fast/scratch/hyaku/kotob | d1c031833c37af99196f72f84a6643f84eec129a, cb93b3a88e1fe0dd35931d40adc66c8f1f4881c9, 173840364, 173865724 | omp root semantics grounded 12 of 12 ; omp root semantics grounded 12 of 12 |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/header-scan.txt` | 138 | U | module headers in ELF: 3131; span 166865730..194305276 | 166865730, 194305276 | none recorded |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/selftest.txt` | 39 | U | 0 failure(s) over 35 assertions | — | none recorded |
| `.ufo/waves/round-87/w3/CriticSemanticsR87/upstream.txt` | 2705 | U | # upstream can1357/oh-my-pi v18.15.0 raw fetch (read-only), fetched 2026-11-05T03:15:55Z | — | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/c1-rev-tip.txt` | 1686 | U | rev 760e1c5edfdefb4767420f711d08f669952de013 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 | 760e1c5edfdefb4767420f711d08f669952de013, 173819979, 173840364, 173865724 | rev 760e1c5edfdefb4767420f711d08f669952de013 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show 760e1c5edfdefb4767420f711d08f669952de013:verifiers |
| `.ufo/waves/round-87/w3/ExecMirrorR87/c2-35a-clone.txt` | 495 | U | PASS d1  two receipts carry exit=0; instruments equal 04647b0f..35a395a9 | 04647b0f, 35a395a9 | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/c2-35a395a9-clone.txt` | 116 | U | could-not-evaluate: worktree tip 760e1c5edfde != measured revision 35a395a9aabf (plans/rou | 760e1c5edfde, 35a395a9aabf | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/c2-clone-placed.txt` | 510 | U | PASS d1  two receipts carry exit=0; instruments equal 04647b0f..760e1c5e | 04647b0f, 760e1c5e | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/c2-rev-tip.txt` | 510 | U | PASS d1  two receipts carry exit=0; instruments equal 04647b0f..760e1c5e | 04647b0f, 760e1c5e | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/gate-35a-clone.txt` | 259 | U | reds: ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead'] | 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1 | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/gate-clone-placed.json` | 4669 | U | { | 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1, 7bb48f213ac677f943d5c791199ed3dddf302f00, 25cc5c7b, fb6a28ee | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/gate-clone.err` | 0 | U |  | — | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/gate-clone.json` | 4756 | U | { | 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1, 7bb48f213ac677f943d5c791199ed3dddf302f00, 25cc5c7b, fb6a28ee | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/gate-lane.err` | 0 | U |  | — | none recorded |
| `.ufo/waves/round-87/w3/ExecMirrorR87/gate-lane.json` | 4669 | U | { | 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1, 7bb48f213ac677f943d5c791199ed3dddf302f00, 25cc5c7b, fb6a28ee | none recorded |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87.md` | 6083 | U | # ExecProbeBoundR87 ? r87-w3 bounded read-only probe of C1's `{cwd}/` bound (conjunct 4) | 760e1c5edfdefb4767420f711d08f669952de013, 760e1c5e | and `HOME=<scratch>/home`, the non-interactive enumeration of omp v18.15.0 is the verb beh ; `omp skill list --json` (the `skill` registry command's local-discovery `list` action; rec |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87/omp_help.txt` | 16905 | U | omp v18.15.0 | — | omp v18.15.0 ; $ omp [COMMAND] |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87/omp_skill_help.txt` | 1552 | U | Install, search, publish, and manage skills on the Skillshare registry (skills.omp.sh) | — | $ omp skill [ACTION] [TARGETS...] [FLAGS] ; omp skill install @alice/pdf-tools |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87/probe-commands-and-observations.md` | 4048 | U | # Probe commands ? ExecProbeBoundR87 (r87-w3, C1 conjunct-4 `{cwd}/` bound) | — | Environment for every omp run below: `env -i HOME="$S/home" TMPDIR="$S" PATH=/home/vgpnk/. ; (with `PATH=/usr/bin:/bin` for the strace run, which execs the omp binary by absolute path |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87/semantics-ledger-760e1c5e.tsv` | 1939 | U | root_pattern?binary_quote?module?reader_quote | — | {cwd}/.omp/skills	Native OMP configuration from ~/.omp and .omp/	coding-agent/src/discover ; ~/.omp/agent/skills	Native OMP configuration from ~/.omp and .omp/	coding-agent/src/discov |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87/skill_list.txt` | 139 | U | local-skill?Cwd-chain probe skill for the r87-w3 {cwd}/ bound probe. | — | none recorded |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87/skill_list_json.txt` | 709 | U | {"skills":[{"name":"local-skill","description":"Cwd-chain probe skill for the r87-w3 {cwd} | — | none recorded |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87/skill_list_outside.txt` | 356 | U | {"skills":[{"name":"probe-skill","description":"Home-level probe skill for the r87-w3 {cwd | — | none recorded |
| `.ufo/waves/round-87/w3/ExecProbeBoundR87/strace_skilllist.txt` | 63392 | U | 565634 execve("/home/vgpnk/.local/bin/omp", ["/home/vgpnk/.local/bin/omp", "skill", "list" | 30b98c4e, 1793848207, 759000000, 122204136 | none recorded |
| `.ufo/waves/round-87/w3/ExecTipR87/SUMMARY.json` | 6733 | U | { | 760e1c5edfdefb4767420f711d08f669952de013, 04647b0f, 760e1c5e, ae3f49a3 | "line": "omp root semantics grounded 12 of 12", ; "d1": "PASS (receipts via git show; instrument equality via git diff --quiet LANDING..REV  |
| `.ufo/waves/round-87/w3/ReviewC1R87.md` | 5355 | U | # ReviewC1R87 ? w3 independent re-implementation of C1 (read-only) | 760e1c5edfdefb4767420f711d08f669952de013, 87ab1cb9, 760e1c5e, 173914936 | \| lane tip \| `git rev-parse master` → `760e1c5edfdefb4767420f711d08f669952de013` (matches  ; \| frozen counter run \| `python3 -B verifiers/check_omp_root_semantics.py --rev 760e1c5e` → |
| `.ufo/waves/round-87/w3/ReviewC1R87/counter_c1_tip.txt` | 1677 | U | rev 760e1c5edfdefb4767420f711d08f669952de013 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 | 760e1c5edfdefb4767420f711d08f669952de013, 173819979, 173840364, 173865724 | rev 760e1c5edfdefb4767420f711d08f669952de013 elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show 760e1c5edfdefb4767420f711d08f669952de013:verifiers |
| `.ufo/waves/round-87/w3/ReviewC1R87/reimpl.py` | 7824 | U | #!/usr/bin/env python3 | 669f2801c31ef27e18cc35a327d2e18f466281c7, 760e1c5edfdefb4767420f711d08f669952de013 | # Reads both ledgers from the tip's committed bytes (git show), maps the installed ; reasons.append("reader_quote not located in the omp ELF") |
| `.ufo/waves/round-87/w3/ReviewC1R87/reimpl_out.txt` | 1291 | U | row  1 GROUND '{cwd}/.omp/skills' module='coding-agent/src/discovery/builtin.ts' @17381997 | 173819979, 173840364, 173865724, 173879095 | guard S1 committed-bytes PASS (both ledgers via git show) |
| `.ufo/waves/round-87/w3/ReviewC1R87/verdicts_diff.txt` | 59 | U | disagreements: none (12/12 identical verdicts and offsets) | — | none recorded |
| `.ufo/waves/round-87/w3/ReviewD1D5R87.md` | 11235 | U | # ReviewD1D5R87 ? independent read-only re-check of C2's five items at 760e1c5 | 760e1c5, 26daaa13, 760e1c5edfdefb4767420f711d08f669952de013, 35a395a9 | \| **D1** \| PASS \| blobs: `git rev-parse 760e1c5e:.ufo/waves/round-86/receipts/{tip-catalog ; \| **D5(i)/(ii)** \| PASS \| blobs at tip equal blobs at base `223ae624`: `round-86-verifier- |
| `.ufo/waves/round-87/w3/ReviewD1D5R87/integrity-tip.json` | 4669 | U | { | 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1, 7bb48f213ac677f943d5c791199ed3dddf302f00, 25cc5c7b, fb6a28ee | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/c1-independent.txt` | 1286 | U | elf sha256 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f pinned True \|  | d1c031833c37 | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/c1-probe.txt` | 3712 | U | elf sha256 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f pinned True | 347639993, 347680750, 347731468, 347758220 | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/c2-independent-tip.txt` | 543 | U | rev d1c031833c37af99196f72f84a6643f84eec129a | d1c031833c37af99196f72f84a6643f84eec129a, 04647b0f, 9b040edb, ae3f49a3 | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/clone-gate.json` | 4756 | U | { | 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1, 7bb48f213ac677f943d5c791199ed3dddf302f00, 25cc5c7b, fb6a28ee | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/indep_c1.py` | 3156 | U | # Independent C1 re-derivation: no import of verifiers/check_omp_root_semantics.py. | — | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/indep_c2.py` | 4138 | U | # Independent C2 re-derivation (D1-D4 from committed bytes; D5 from blobs + the measured g | 223ae62424f8ab1eb365d733eb648d6228ddd7e8 | and "omp catalogue lines reproduced 215 of 215" in cat |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/item1-item3.txt` | 1579 | U | item 1 ? non-author records, base 223ae624 vs tip | 223ae624, 223ae62, ae3f49a3685e796ae5154cf9a4b055132a8c25b0, 760e1c5 | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/item2-tmp-hits.txt` | 2031 | U | corpus hits: 57 \| .ufo/waves/round-87 hits: 2 | — | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/item4-credentials.txt` | 1229 | U | command: | — | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/item5-ready.txt` | 1862 | U | === ready files under .ufo/waves/round-87/ | 9b040ed, d1c0318 | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/item6-confinement.txt` | 1496 | U | === brief tip vs measured tip | 760e1c5edfdefb4767420f711d08f669952de013, d1c031833c37af99196f72f84a6643f84eec129a, d1c0318, 760e1c5 | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/measurements-C1-C2.txt` | 1850 | U | measured at 2026-11-05T00:16:58-03:00; lane master = d1c031833c37af99196f72f84a6643f84eec1 | d1c031833c37af99196f72f84a6643f84eec129a, 173819979, 173840364, 173865724 | rev d1c031833c37af99196f72f84a6643f84eec129a elf /home/vgpnk/.local/bin/omp sha256 6737ee2 ; guard S1 ledger-from-rev PASS (git show d1c031833c37af99196f72f84a6643f84eec129a:verifiers |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/non-author-blobs.txt` | 295 | U | == corpus/lessons/round-86-verifier-spotcheck.md | ae3f49a3685e796ae5154cf9a4b055132a8c25b0, 315c0ec68075e9c7c4037b8f42617e3eee0a434b | none recorded |
| `.ufo/waves/round-87/w3/SentinelEvidenceR87/probe_c1.py` | 3017 | U | import hashlib, mmap, re, subprocess, sys | — | none recorded |
| `.ufo/waves/round-87/w3/l1/base-both.txt` | 437 | T | # L1 receipt ? both frozen counters at the base, run 2026-11-05T00:08:55-03:00 | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 760e1c5edfde, 223ae62424f8 | $ rev=223ae62424f8ab1eb365d733eb648d6228ddd7e8 ; $ python3 -B verifiers/check_omp_root_semantics.py --rev $rev |
| `.ufo/waves/round-87/w3/l1/battery-at-d1c03183.txt` | 2666 | U | measured rev d1c031833c37af99196f72f84a6643f84eec129a in a fleet-shaped sandbox; base 0720 | d1c031833c37af99196f72f84a6643f84eec129a, 072048fa8e8a52c707d25f7079772fa317244eb7 | none recorded |
| `.ufo/waves/round-87/w3/l1/c1-tip.txt` | 1894 | T | # L1 receipt ? C1 at the round tip (2026-11-04T23:59:17-03:00) | 760e1c5edfdefb4767420f711d08f669952de013, 173819979, 173840364, 173865724 | $ git rev-parse master ; $ python3 -B verifiers/check_omp_root_semantics.py --rev $(git rev-parse master) |
| `.ufo/waves/round-87/w3/l1/c2-base-clone.txt` | 1762 | T | # C2 counter at the base ? what the frozen instrument can and cannot measure | 223ae62424f8ab1eb365d733eb648d6228ddd7e8, 26daaa13, 760e1c5edfde, 223ae62424f8 | $ git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin $S/repo ; $ git -C $S/repo checkout -q -B master 223ae62424f8ab1eb365d733eb648d6228ddd7e8 |
| `.ufo/waves/round-87/w3/l1/floors-standalone.txt` | 234 | U | PASS harness observed=34 floor=10 | — | none recorded |
| `.ufo/waves/round-87/w3/l1/instrument-sha256.txt` | 314 | T | 6e826f3bf8d4585340ddcc9b7a546e4b7d8b9774a2794c4f45b3cf13e7798922  verifiers/check_omp_root | — | none recorded |
| `.ufo/waves/round-87/w3/l1/q79-control.txt` | 1533 | T | # Q79 location control ? run 2026-11-04T23:59:40-03:00 | 760e1c5edfdefb4767420f711d08f669952de013, 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1 | $ python3 -B .ufo/waves/round-87/w3/l1/q79_location_control.py --rev $(git rev-parse maste |
| `.ufo/waves/round-87/w3/l1/q79_location_control.py` | 5635 | T | #!/usr/bin/env python3 | — | python3 -B q79_location_control.py --rev <rev> [--keep] [--work DIR] |
| `.ufo/waves/round-87/w3/swarm-registry.json` | 3967 | T | { | — | none recorded |

Receipt command provenance: `receipts/base-battery.txt` and `after-battery.txt` carry no command lines; their commands are the scripts `build-base-battery.sh` and `build-after-battery.sh` (in the tree). `receipts/c1-*.txt`, `c2-*.txt` and `census-after.txt` name no command; the C1 counter's own `--rev` line and the C2 PASS lines are the only provenance inside the file.

## 2. Section headings with line numbers

### `corpus/lessons/round-87.md` (159 lines)

| line | heading |
|---:|---|
| 1 | # Round 87 — kotoba (attempt 1, Linux host, omp/18.15.0) |
| 9 | ## Claims (verbatim from the freeze) |
| 33 | ## Gate |
| 47 | ## Census (`corpus/SOURCES.md`, contract v1) |
| 56 | ## Mistakes |
| 84 | ## D5 disclosure (the two remaining DRIFTs, `left red and disclosed`) |
| 93 | ## Routed to the next round |
| 102 | ## Attempt 2 — re-verification at the round tip (driver cycle 2, attempt 1) |
| 135 | ## Mistakes |
| 153 | ## Gate — attempt 2 |

### `plans/round-87.md` (209 lines)

| line | heading |
|---:|---|
| 1 | # kotoba round 87 — plan and freeze |
| 23 | ## C1 — depth (score 9, owned lowest): root semantics grounded per root |
| 92 | ## C2 — consistency (calibration sub-axis, score 10): the five routed r86 defects close |
| 142 | ## Kill rule (instrument boundary) |
| 153 | ## No-harm battery |
| 164 | ## Touch list |
| 174 | ## Frontier step (§2b, `CORPUS.md` contract v1) |
| 193 | ## Round shape (hyaku run 15, band 8–16) |
| 203 | ## Admission |

### `plans/round-87-addendum-1.md` (64 lines)

| line | heading |
|---:|---|
| 1 | # kotoba round 87 — addendum 1 (committed before the first candidate score) |
| 7 | ## A1.1 — C1's denominator is 12, not 13 |
| 46 | ## A1.2 — C2's D5 is measured in the lane worktree, not in a clone |
| 60 | ## A1.3 — what does not change |

### `plans/round-87-addendum-2.md` (71 lines)

| line | heading |
|---:|---|
| 1 | # kotoba round 87 — addendum 2 (committed before the first candidate score) |
| 7 | ## A2.1 — D5 measures "the carried base red is carried honestly", not "the gate is green" |
| 55 | ## A2.2 — the laundering attempt, reverted (the round's mined mistake M87-1) |
| 67 | ## A2.3 — what does not change |

## 3. LOG.md and SCORECARD.md round-87 entries

`grep -n 'Round 87' LOG.md` → 3298 (`## Round 87 — two claims`), 3351 (`### Round 87, attempt 2`). `grep -n 'Round 87' SCORECARD.md` → 601 (`## Round 87 — two claims`).

- LOG.md round-87 block: lines 3298–3372 (to end of file; no later `##` heading).
- SCORECARD.md round-87 block: lines 601–648 (to end of file; no later `##` heading).

Commit-hash resolution for every hash cited in the two blocks and in the four round documents (`git cat-file -t`, lane first then fleet; a blob is an object, not a commit):

| cited at | token | object type | repo |
|---|---|---|---|
| `corpus/lessons/round-87.md:3` | `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | commit | lane |
| `corpus/lessons/round-87.md:4` | `669f2801c31ef27e18cc35a327d2e18f466281c7` | commit | lane |
| `corpus/lessons/round-87.md:5` | `512126bbd762ff82b9f330c4afefb29db7cd9f39` | commit | lane |
| `corpus/lessons/round-87.md:6` | `87ab1cb98b4950f5d7291a4a2ddaab535ca72124` | commit | lane |
| `corpus/lessons/round-87.md:49` | `223ae62` | commit | lane |
| `corpus/lessons/round-87.md:66` | `7d9f599` | blob | lane |
| `corpus/lessons/round-87.md:66` | `d7f589b` | blob | lane |
| `corpus/lessons/round-87.md:66` | `ae3f49a` | blob | lane |
| `corpus/lessons/round-87.md:66` | `315c0ec` | blob | lane |
| `corpus/lessons/round-87.md:89` | `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1` | ABSENT | neither lane nor fleet |
| `corpus/lessons/round-87.md:105` | `760e1c5edfdefb4767420f711d08f669952de013` | commit | lane |
| `corpus/lessons/round-87.md:106` | `d752fdbe9cdf82a6faff730d44f44c6fa3e3eb00` | commit | fleet |
| `corpus/lessons/round-87.md:111` | `760e1c5e` | commit | lane |
| `corpus/lessons/round-87.md:120` | `5b052020a13b37340c1054286d65b2514c7133d5` | commit | fleet |
| `corpus/lessons/round-87.md:129` | `35a395a9` | commit | lane |
| `plans/round-87.md:6` | `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | commit | lane |
| `plans/round-87.md:112` | `04647b0f715ff3c4f314b0d8f03dea28bc453688` | commit | lane |
| `plans/round-87.md:156` | `223ae62` | commit | lane |
| `plans/round-87.md:179` | `223ae62` | commit | lane |
| `plans/round-87-addendum-1.md:3` | `669f2801c31ef27e18cc35a327d2e18f466281c7` | commit | lane |
| `plans/round-87-addendum-1.md:36` | `669f280` | commit | lane |
| `plans/round-87-addendum-2.md:3` | `669f2801c31ef27e18cc35a327d2e18f466281c7` | commit | lane |
| `plans/round-87-addendum-2.md:3` | `512126bbd762ff82b9f330c4afefb29db7cd9f39` | commit | lane |
| `plans/round-87-addendum-2.md:13` | `223ae62` | commit | lane |
| `plans/round-87-addendum-2.md:27` | `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1` | ABSENT | neither lane nor fleet |
| `plans/round-87-addendum-2.md:38` | `223ae62` | commit | lane |
| `LOG.md:3300` | `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | commit | lane |
| `LOG.md:3300` | `669f2801` | commit | lane |
| `LOG.md:3301` | `512126bb` | commit | lane |
| `LOG.md:3301` | `87ab1cb9` | commit | lane |
| `LOG.md:3312` | `223ae62` | commit | lane |
| `LOG.md:3319` | `04647b0f` | commit | lane |
| `LOG.md:3328` | `ae3f49a` | blob | lane |
| `LOG.md:3328` | `315c0ec` | blob | lane |
| `LOG.md:3329` | `7d9f599` | blob | lane |
| `LOG.md:3329` | `d7f589b` | blob | lane |
| `LOG.md:3341` | `9b040ed` | commit | lane |
| `LOG.md:3355` | `760e1c5e` | commit | lane |
| `LOG.md:3355` | `d752fdbe` | commit | fleet |
| `LOG.md:3357` | `760e1c5e` | commit | lane |
| `LOG.md:3361` | `35a395a9` | commit | lane |
| `SCORECARD.md:607` | `223ae62424f8ab1eb365d733eb648d6228ddd7e8` | commit | lane |
| `SCORECARD.md:609` | `e03f9e226b51b8cb94f2dc5c7c3027c5286b004b` | commit | lane |
| `SCORECARD.md:620` | `ff4bf3fd70662f20ab066eee6fde4bd605aa07b6` | commit | lane |
| `SCORECARD.md:639` | `760e1c5e` | commit | lane |

## 4. Missing evidence (pointer named in a round-87 record, not on disk)

| cited at | pointer text | status |
|---|---|---|
| LOG.md:3370 | `.ufo/waves/round-87/w3/l1/census-now.txt` | absent from the tree (dangling) |
| plans/round-87.md (§ No-harm battery, Q73 sweep line) | `receipts/q73-sweep.txt` | absent; the sweep is a `q73_sweep` section inside `receipts/base-battery.txt` (build-base-battery.sh), so the promised separate receipt does not exist |
| corpus/lessons/round-87.md:96 | `Sentinel.md` (w1 attack seat, named with `ReviewerC1.md`) | absent: `.ufo/waves/round-87/w1/Sentinel.md` does not exist; `w1/ReviewerC1.md` does |
| corpus/lessons/round-87.md:89 and plans/round-87-addendum-2.md:27 | commit `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1` | absent from lane and fleet; dangling by design and disclosed (D5 disclosure), so not a defect of the record |
| plans/round-87.md:185–187 (Assimilation) | `/home/vgpnk/Projects/shokuknow/merge/kotoba/` reported "absent on this host" | PRESENT: the directory exists (MERGE-REPORT.json, MERGE-REPORT.md, SOURCES.append.md; mtime 2026-10-24T23:33), so the plan's stated premise for `Assimilation: none` is false; the lesson carries no `Assimilation:` line at all |

Pointers that are not dangling but resolve only at the fleet root (not in the lane): `.ufo/l0-questions.md` (plans/round-87.md:18), `scripts/hyaku/ufo-wave-policy.json` (plans/round-87.md:195), `.ufo/watchdog.log` (LOG.md:3353), `.ufo/reports/round-84/kama.md` (lesson:61, lesson:86, addendum-2:22, LOG.md:3360, SCORECARD.md:641). The three `/home/u/proj/…` tokens at plans/round-87.md:65 are the frozen synthetic ancestor chain, not pointers, and are excluded from the count.

Pointer sites counted: 160 (scan 158 path/hash citation sites + 2 bare-name sites found by reading). Resolved 155, dangling 5 (of which 2 are the disclosed `8b1cc1b…` by design).

index: 129 files, 155 resolved pointers, 5 dangling
