# R03RevR1Text — R1 correction-draft verdict

The `.ufo/waves/round-76/build/B08-r1-round-75-correction.diff` is accurate and append-only. It names and quotes the superseded M75-1 row and Gate reject candidate, withdraws the stale-premise classification and reject, fixes the count using the whole YAML folded scalar, and addresses the related plan note. No corrected replacement text is needed.

Independent measurement at the specified r75 tip:

`git show ac9f29510d3914a6edb97c8dbdb3445cab9141de:SKILL.md | python3 -c 'import sys,yaml; d=yaml.safe_load(sys.stdin.read().split("---")[1])["description"]; print(len(d),len(d.strip()),len(d.strip().split(". ")[0]+"."))'`

Output: `1022 1021 151` (exit 0). This matches the clip-preserving 1,022 convention stated in round-76 addendum 1 and the 1,021 stripped variant.

The diff adds a correction section; the superseded row is quoted as an indented block, not rewritten or left as a live row. The source spot-check §6 R1 calls for a named appended correction and re-derivation; the draft explicitly withdraws the related `plans/round-75.md:15` premise and says r75 C1 did not consume it. The root `CORPUS.md` named in the assignment is not present in this lane tree, so its exact text was not independently checked; the append-only/new-entry behavior is evident in the diff itself.

VERDICT: Accept; no correction text needed.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/R03RevR1Text.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/R03RevR1Text.md