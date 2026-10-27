Seat: Kb79S07BudgetCensus — proposal 1 measurement + SKILL.md budget (Q65)

Evidence source and method

Read-only scratch checkout at base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`; measurements were of `git show <base>:<path>` output, not the current working tree. Commands used for each file `<f>`:

- `git show b10bcbc6b00f8f56b202ccbadca311007b5b463c:<f> | wc -c`
- `git show b10bcbc6b00f8f56b202ccbadca311007b5b463c:<f> | wc -l`
- For each N=120, 200, 300: `git show ...:<f> | awk -v n=N 'length>n' | wc -l`
- `git show ...:<f> | awk 'length>m{m=length}END{print "longest="m}'`

| File at base | bytes (`wc -c`) | lines (`wc -l`) | lines >120 chars | lines >200 chars | lines >300 chars | longest line chars |
|---|---:|---:|---:|---:|---:|---:|
| `SKILL.md` | 78,647 | 590 | 147 | 129 | 77 | 1,095 |
| `corpus/README.md` | 83,225 | 306 | 154 | 130 | 102 | 2,385 |

Section byte command: `git show <base>:SKILL.md | awk 'BEGIN{section="(preamble)"} /^## /{section=$0} {bytes[section]+=length($0)+1} END{for(s in bytes) print bytes[s],s' | sort -nr`. Results: `## Gate registry` 24,809 B (31.5% of the wc byte total; awk includes one newline per split line); `## Instruction surfaces — pick the file before the fix` 17,489 B; `## Frontmatter craft — the trigger surface` 8,615 B; `## Trigger-fidelity checklist` 6,429 B; `## Sources` 5,826 B; `(preamble)` 3,621 B; `## Agent-definition fidelity checklist` 2,869 B; `## Anti-patterns` 2,586 B; `## Compression rules` 2,111 B; `## Dispatch-prompt fidelity checklist` 1,896 B; `## Always-on constraint-file checklist (AGENTS.md-class)` 1,347 B; `## Refusals` 402 B; `## Router model — which harness, which gate` 253 B.

Gate impacts and sortedness

Search command requested: `grep -nE '600|line_budget|budget' verifiers/*.py | head -40`. Specialized source search (`grep` tool, same expression over verifier sources) found the relevant size check in `verifiers/verify_skill_checklist.py`: check id `trigger.line_budget`. Its documented rule binds to the first integer in the checklist text matching a file/line bound, currently “File ≤ 600 lines”; otherwise its `--max-lines` default is 600. The check counts lines, not bytes. No verifier size gate or byte pin was found by this sweep; the other search hits were timeout/runtime or unrelated budget uses. The located check is the only relevant SKILL.md line-count gate evidenced by that sweep.

At base 590 lines, the plan's proposed +7 lines yields 597, below the 600-line bound, so that addition alone does not trip `trigger.line_budget`. The current byte count already exceeds a proposed 70,000-byte ceiling by 8,647 bytes; therefore that ceiling would be red-before at this base. No currently located gate pins SKILL.md bytes. `check_gate_registry.py` parses registry rows beneath the exact `## Gate registry` heading, validates row content and exactly-one-row-per-verifier, and does not test row ordering. Rows need not be inserted in sorted position for that check; sorting could still be a readability convention, but it is not enforced by this verifier.

Proposal-only recommendation (not a claim this round)

A falsifiable initial ceiling is `SKILL.md <= 70,000 bytes`, measured by `wc -c < SKILL.md`; red-before is directly observed at base: 78,647 bytes, i.e. 8,647 over. This makes the suggested ceiling an actual discriminating test rather than a bound that already passes, unlike the existing 600-line ceiling (590 at base). It is a proposal only; no lane rule or claim is made here. The planned +~2.5 KB would not cure the base violation and would raise the amount requiring reduction to roughly 11.1 KB versus the ceiling.

Commands and exit statuses

- Disk guard: `/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status` — exit 0; scratch measurement then completed.
- Scratch clone/checkout and all metric commands above completed successfully; their emitted values are transcribed in the table. No verifier was executed for this seat.
- Cleanup: scratch tree removed by the command's EXIT trap.

VERDICT: Base SKILL.md is 78,647 B / 590 lines; a 70,000-byte ceiling would be falsifiably red-before, while the proposed +7 lines remain within the existing 600-line gate.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79S07BudgetCensus.md