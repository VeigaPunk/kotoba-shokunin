# Kb80R04SiblingScan — sibling-lane allowed-tools overlap scan

Seat: Kb80R04SiblingScan (leaf scout, round 80 w1)
Question: does any sibling lane repo under /home/vgpnk/Projects/shokunin already hold
`allowed-tools` knowledge — a per-client semantics matrix (C2's claimed ground) or even a
key-name mention — such that C2 would overlap/adjoin existing fleet ground?

## Answer

NO. No sibling lane holds this ground. The only fleet repo with lane-authored
`allowed-tools` knowledge is kotoba-shokunin itself. Overlap = none; adjacency = none.
C2's ground is novel fleet-wide; there is no sibling matrix to port from and no
adjacency block. (This is freshness/depth-positive for C2, not a defect.)

## Coverage of the sweep (so the negative is real, not an artifact)

All 20 sibling lanes (`*-shokunin` under the fleet root, kotoba-shokunin excluded) were
swept. Every one has a corpus/knowledge dir (5–253 files each); 18/20 have SKILL.md
(audio-shokunin and game-dev-2d-shokunin do not).

## Commands and exit codes

1. Spec-mandated sweep, per lane:
   `grep -rl 'allowed-tools' <lane>/corpus/knowledge <lane>/SKILL.md 2>/dev/null`
   across all 20 siblings → 0 hits (sweep loop exited clean; SCAN-DONE).
2. Variant sweep (hyphen/underscore/space/camel):
   `grep -rlE 'allowed[-_ ]?tools|allowedTools' /home/vgpnk/Projects/shokunin/*/corpus/knowledge /home/vgpnk/Projects/shokunin/*/SKILL.md` (siblings only)
   → 0 hits, exit rc=1 (VARIANT-DONE rc=1).
3. Whole-corpus sweep incl. evidence/ subdirs:
   `grep -rl 'allowed.tools' /home/vgpnk/Projects/shokunin/*/corpus` (siblings only)
   → 2 hits, BOTH in tabi-shokunin vendored third-party data (see Hit 1).
4. Concept-paraphrase sweep:
   `grep -rliE 'tool.?allowlist|permitted.?tools|grant.?semantics|allow.*tool.*surface' <sibling corpus/knowledge + SKILL.md>`
   → 1 hit, tsukuroi (see Hit 2).
5. Fleet non-lane dirs (templates/, research/, scripts/):
   `grep -rl 'allowed-tools' ...` → 0 hits, rc=1.

## Hit list (every hit found, classified)

- Hit 1 (key-name mention, NOT lane knowledge): tabi-shokunin —
  corpus/evidence/round-13/aria/node_modules/playwright-core/lib/tools/skills/playwright-cli/SKILL.md
  and .../playwright-trace/SKILL.md. Content: the vendored Playwright CLI skill's
  frontmatter line `allowed-tools: Bash(playwright-cli:*) Bash(npx playwright:*) ...`.
  Classification: third-party node_modules captured as round-13 evidence data; a bare
  key-name usage, not a per-client semantics matrix, not authored by the tabi lane.
  Corroborating side-observation: the `allowed-tools:` frontmatter key is real in the
  wild (Playwright ships it), which is mild external corroboration for C2's form-level
  claim — data point, not lane ground.
- Hit 2 (adjacent concept, NOT allowed-tools ground): tsukuroi-shokunin —
  corpus/knowledge/seat-boundary-r22.md:22. Discusses `task.tools` adding eval-defined
  tools for seat dispatch and a request auditor that "fails closed on unknown tools";
  the text itself states it "is not a native-tool allowlist" and claims "no native
  toolset restriction". Classification: seat tool-binding audit semantics, adjacent in
  theme (tool restriction) but unrelated to the allowed-tools frontmatter key and to
  any per-client grant-semantics matrix.

No sibling file is a per-client allowed-tools semantics matrix; no sibling SKILL.md or
lane-authored knowledge file mentions the `allowed-tools` key at all.

## Contrast: where the ground actually lives (kotoba only)

Exact-string `allowed-tools` counts in kotoba-shokunin (for the adjacency line):
- corpus/knowledge/frontmatter-rule-authorities-round48.md — 2 mentions
- corpus/knowledge/chinese-vendor-skill-surfaces-round73.md — 5 mentions
- corpus/knowledge/agent-definition-files-round56.md — 0 exact (variant sweep hit was
  the substring `disallowedTools`, a denylist key, not allowed-tools)
- SKILL.md — 0 exact (same `disallowedTools` substring via the variant regex)

## Remaining unknowns

- None for the assigned question. Sibling private state (.ufo waves of other rounds)
  was not exhaustively grepped — the spec scoped the scan to corpus/knowledge and
  SKILL.md, plus my two broader corroborating sweeps (whole corpus incl. evidence;
  concept paraphrases). Those broader sweeps are sufficient to make "no sibling holds
  this ground" a grounded negative: the only hits anywhere in sibling trees are the
  two vendored Playwright files and the one tsukuroi seat-boundary paragraph.

## Adjacency verdict for the report line

Sibling overlap scan: NO sibling lane holds allowed-tools ground (no per-client
semantics matrix, no lane-authored key-name mention). Only kotoba-shokunin carries the
ground. Overlap = none → adjacency evidence = none; C2 is fleet-novel.

VERDICT: No sibling holds allowed-tools ground; only vendored Playwright data (tabi) and an unrelated tool-binding note (tsukuroi) match even broad sweeps — C2 has zero fleet overlap.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80R04SiblingScan.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80R04SiblingScan.md
