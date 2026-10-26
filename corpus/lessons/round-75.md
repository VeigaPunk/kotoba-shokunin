# Round 75 lessons — kotoba

## Gate

Source opened this round: https://agentskills.io/skill-creation/optimizing-descriptions.md (2026-10-27). Located quote (page heading “Writing effective descriptions”): “Use imperative phrasing.” (3 words). This source is existing row S213, not a new row; a new knowledge entry must cite S213. Candidate admit: description evaluation guidance may be admitted only as scoped advice, with a controlled held-out query experiment; no current experiment has been run. Candidate reject: any claim that the 1021-character description size reported in `considerthese/2026-10-26.md` remains current; current frontmatter is materially shorter. Non-author admit/reject spot-check: pending; dispatched wave members are lane seats and do not qualify.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| stale-premise | `considerthese/2026-10-26.md:17` says description is 1,021/1,024 characters; current committed SKILL frontmatter (master 65a5c7a, lines 3–18) is substantially shorter; direct `awk 'NR>=3&&NR<=8{print NR ":" length($0) ":" $0}'` yields 14,76,78,73,79,72 for frontmatter lines 3–8. | Q67 (read proposal against actual file contract) does not catch stale values; corpus Q54/Q60 require reproducible counts and revision-addressed evidence, but no current criterion catches a proposal's imported observation | Freeze each proposed target from the current committed bytes and rerun its counter before plan freeze; classify historical proposal numbers as historical, not as round baseline. This lesson-only repair is not claimed as a guard until a failing fixture demonstrates it. |
| attribution | Fleet misroot sweep found seat report `kotoba-shokukin/.ufo/waves/round-75/w1/R75Facet48.md` outside the lane; `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed `?? kotoba-shokukin/`, and `find` located the report. | Q49 (seat reports must stay lane-local and the final misroot sweep covers every seat-writable directory) | Copied byte-exact to the same relative lane path, verified with `cmp`, then removed only the fleet-root copy; report the misplaced original and recovery. |
