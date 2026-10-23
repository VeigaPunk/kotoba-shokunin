Result: HOLDS — the ed3e8996 budget move is verbatim byte for byte, the two replacement lines state no new fact and drop no rule a SKILL.md-only reader cannot reach in one hop, and both named verifiers pass at tip.

# Review: SKILL.md § Anti-patterns budget move (commit ed3e8996)

Scope: `git show f0e5de82:SKILL.md | sed -n 407,426p` vs the appended section of
`corpus/knowledge/skill-overlap-levers-round51.md` at
f0e6b695b746775823b65a8c45de7d50ea33e84f; the two replacement lines at tip SKILL.md:421 and :423;
`check_overlap_levers.py` and `verify_skill_checklist.py` (line budget). All work in a sandbox clone
at `/fast/scratch/hyaku/kotoba-r55/ReviewSkillMove` checked out at the tip; the lane was touched
read-only only.

## Check 1 — byte-for-byte move: PASS

- `git show f0e5de82:SKILL.md | sed -n '407,426p'` → 20 lines, sha256
  `1423f8ce569b3e409541b984694f017fe56fc0792946027743ac68b71c4b6c19`.
- The appended `## Moved from 'SKILL.md' § Anti-patterns (round 55, verbatim)` section in the tip
  knowledge file spans lines 146-171; its body (lines 152-171, from `Error pattern` through
  `...check_overlap_levers.py.`) is lines 152-171 = 20 lines, sha256
  `1423f8ce569b3e409541b984694f017fe56fc0792946027743ac68b71c4b6c19` — `diff` empty, `cmp` clean.
- Boundary check: f0e5de82 SKILL.md:405 is `location; durable policy copy-pasted into a dispatch
  prompt.` (kept) and :427 is blank before the levers table (kept); the 407-426 range is exactly the
  two prose paragraphs.
- The entry's own claim "`SKILL.md` lines 407–426 at `f0e5de82`… moved here byte for byte" is
  accurate. Note: ed3e8996's parent was 9615579 (the C1 table commit), but the moved block sat at
  the same range there (the C1 insertion is above it), so the header's rev reference is correct.

## Check 2 — replacement lines: no new fact; dropped material is one hop away, with two named losses

Tip SKILL.md:421 (Error pattern) — every clause is a fair compression of the moved text: the
pattern, the eight-pages/five-clients reading with the entry citation, and the fix
(`trigger.05`, name the neighbour and split) are all in the original.

Tip SKILL.md:423 (Overlap levers) — the kept claims (one named skill per lever; none decides
between two skills that both stay candidates; the removed skill stops firing automatically; the
checker command) are all in the moved text or its entailment. "…also stops firing automatically"
drops the original qualifier "on prompts only it matches" — this is a faithful cost compression,
not a new claim, because removal from automatic choice was already stated.

Meta-fact added: "moved verbatim in round 55 to … § Moved from `SKILL.md`" — true by Check 1, and
it is a statement about the edit, not a domain fact.

Named drops (all recoverable in one hop via the pointer, except the two key names below):

1. `check_sibling_census.py … --province --skill` invocation — dropped from SKILL.md body. It
   survives verbatim at the pointed-to section, and the script stays in the Gate registry
   (SKILL.md:465). A SKILL.md-only reader loses zero rules, only a copy-pasteable command — same
   shape as the accepted round-15 anti-patterns move ("read it before shipping").
2. `stay under 1,024 characters` — dropped from line 421 but the rule is stated verbatim at
   SKILL.md:181, :185, :187-191 (thresholds table); no reader loses it.
3. The three when-to-use conditions and the ownership rule ("only the levers held by the skill
   author apply to your own skill") — now behind the pointer only. This is the riskiest drop:
   they are usage *rules*, not trivia, and the replacement's "When to use one … : that entry"
   makes the deferral explicit and the table's `held by` column partially encodes the ownership
   rule. Within the brief ("no rule a reader acting on SKILL.md alone needs" — the reader still
   gets pattern, fix, per-client levers, and an explicit pointer), this holds, but it is the seat
   judgment most exposed to a stricter reading.
4. Claude Code `paths` and Copilot CLI `ignoredSkillsLocations` key names — the only dropped
   tokens with no residue anywhere in SKILL.md (grep over tip SKILL.md finds neither outside the
   moved text; they were already marked "not counted below"). Losing them costs the reader the
   two concrete location-split keys; the pointer preserves them in the entry.

No defect found; items 3-4 are the observations a stricter reviewer could route as an over-compression
nit. The replacement lines introduce no unsupported fact.

## Check 3 — verifiers at tip: PASS

- `python3 -B verifiers/check_overlap_levers.py --rev f0e6b695b746775823b65a8c45de7d50ea33e84f`
  (clone, `date -u` Fri 23 Oct 2026 12:14:24 AM UTC): prints `BACKED` x7 then
  `overlap levers backed 7 of 7 clients`, exit 0.
- `python3 -B verifiers/verify_skill_checklist.py` in the lane directory (read-only; no writes to
  the repo): all checks PASS including `trigger.line_budget: evaluated 598 — 598 lines within
  budget 600 (from box at line 300)`, exit 0.

## Verification gaps / environment notes

- Running `verify_skill_checklist.py` inside the scratch clone at
  `/fast/scratch/hyaku/kotoba-r55/ReviewSkillMove` fails on three environment-bound checks —
  `trigger.name_directory` (`'kotoba-shokunin' != directory 'ReviewSkillMove'`) and
  `trigger/governance.citation_resolves` (`../.ufo/reports/...` and `../PROTOCOL.md` resolve
  against the repo's parent, which the scratch path does not have). These are clone-location
  artifacts, not content failures; the lane run at the same tip content is the meaningful result
  and it exits 0.
- The lane working tree currently has uncommitted `SKILL.md` changes (one opencode row in
  `### Explicit invocation by client`, ~line 202) — outside this item's scope; it does not touch
  the moved block, the replacement lines, or the levers table. Line count stays 598.

## No installs

No tools installed or upgraded; stock `git`, `sed`, `diff`, `cmp`, `sha256sum`, `python3` sufficed.
